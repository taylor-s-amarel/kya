import re
import codecs
import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient
import hashlib
import datetime

"""
Purpose:
    Scrapes down information on Employment Agencies from the HK Labor Department's
    Employment Agencies Administration Website.

Returns:
    A csv file with the following Fields
        govid : government issued agency id
        english_name : english name of the agency
        chinese_name : chinese name of the agency
        district : district the agency is registered in
        address : address the agency is registered under
        telephone : phone number of the agency
        fax : fax number of the agency
        email : email address of the agency
        placement_type : what kind of placements the agency is licensed for
        link : the url of the details page for the agency
        lat : latitudinal coordinates of the agency
        lng : longitudinal coordinates of the agency
        valid_license_since : year the agency first became licensed

Runtime:
    At last run, 53 Minutes

Note:
    The information on this Website is updated periodically, but not too
    frequently. As of April 12, 2018, it was last updated March 15, 2018.
    The last update date will be available on the website. Will check on April 15
    to see if the updates run on a monthly timeline.

How does it work:
    We navigate to the "Details" page of every single employment agency. These
    pages can be found easily through agency govt. id. Once at this page, use
    beautifulSoup to extract all relevant information and write it to our csv file.

    employment agency ids that are not longer listed will be passed. We use a simple
    grep for this.


Inner Details/Relevant Thoughts and Findings:
    Employment agencies are given IDs that run the continous
    sequence 1-N, where N is the total number of employment agencies ever registered.
    A good number of IDs are no longer listed on the website. We should look into
    what leads an agency to being delisted at a later point. As our talks with
    Taylor and others would suggest, the number of agencies registering each year
    has been accelerating. There were 576 new registrations last year. Currently,
    the highest registration number is roughly 3800. We can set the UPPER_ID_LIMIT
    roughly higher than this to give us a safe upperbound.

"""
#An arbitrary number above however many registered agencies there are.
def main():
    collectionName = 'employmentAgenciesPH-' + datetime.datetime.today().strftime('%d-%m-%Y')
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
        os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    employmentAgenciesPh = db[collectionName]

    url = "http://www.poea.gov.ph/cgi-bin/agList.asp?mode=all"
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    results = soup.find_all("font", {"face" : "Arial"})
    results = results[6:]
    for i, p in enumerate(results):
        stripped_strings_generator = p.stripped_strings
        stripped_strings = [s.encode('utf8') for s in stripped_strings_generator]
        if len(stripped_strings) == 16:
            del stripped_strings[12]
        agency_name = stripped_strings[0]
        agency_address = stripped_strings[2]
        agency_telephone = stripped_strings[4]
        agency_email = stripped_strings[6]
        agency_website = stripped_strings[8]
        agency_representative = stripped_strings[10]
        agency_status = stripped_strings[12]
        agency_dates = stripped_strings[14]

        print(i)
        print(agency_name)
        print("")

        agency_address = formatAddress(agency_address)
        agency_telephones = formatTelephones(agency_telephone)
        agency_email = formatEmail(agency_email)
        agency_website = formatWebsite(agency_website)
        agency_representative = formatRepresentative(agency_representative)
        agency_status = formatStatus(agency_status)
        license_start_date, license_end_date = formatDates(agency_dates)

        #This is buggy because some agencies might have same name.
        hash_object = hashlib.sha1(agency_name)
        agency_id = hash_object.hexdigest()

        agency_data = {
            "_id": agency_id,
            "name": agency_name,
            "address": agency_address,
            "telephone": agency_telephones,
            "website": agency_website,
            "representative": agency_representative,
            "status": agency_status,
            "license_start_date": license_start_date,
            "license_end_date": license_end_date,
            "email": agency_email
        }
        employmentAgenciesPh.update({"_id": agency_id}, {'$set': agency_data}, upsert=True)

def formatAddress(address):
    address = address.replace(": ", "")
    address = address.replace(":", "")
    address = address.replace("&nbsp", " ") #intentionally whitespace
    address = address.replace(";", "")
    return address

def formatTelephones(telephone):
    telephones = []
    p = re.compile('(\d{3}\-\d{4}|\d{7})')
    matches = p.findall(telephone)
    for match in matches:
        if "-" in match:
            telephones.append(match.replace("-", ""))
        else:
            telephones.append(match)
    return telephones

def formatEmail(email):
    email = email.replace(":", "")
    email = email.replace(" ", "")
    email = email.replace("&nbsp", "")
    email = email.replace(";", "")
    if "@" not in email:
        return ""
    return email

def formatWebsite(website):
    website = website.replace(":", "")
    website = website.replace(" ", "")
    website = website.replace("&nbsp", "")
    website = website.replace(";", "")
    if "." not in website:
        return ""
    return website

def formatRepresentative(rep):
    rep = rep.replace(": ", "")
    rep = rep.replace(":", "")
    rep = rep.replace("&nbsp", " ")
    rep = rep.replace(";", "")
    return rep

def formatStatus(status):
    status = status.replace(": ", "")
    status = status.replace(":", "")
    status = status.replace("&nbsp", " ")
    status = status.replace(";", "")
    return status

def formatDates(date):
    date = date.replace(": ", "")
    date = date.replace(":", "")
    date = date.replace("&nbsp", "")
    date = date.replace(";", "")
    p = re.compile('\d{1,2}\/\d{1,2}\/\d{4}')
    matches = p.findall(date)
    if len(matches) <= 1:
        return (None, None)
    return (matches[0], matches[1])

if __name__ == "__main__":
    main()
