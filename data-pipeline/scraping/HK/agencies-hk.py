import re
import codecs
import requests
from bs4 import BeautifulSoup
import os
from pymongo import MongoClient
import datetime
import time

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
    collectionName = 'employmentAgenciesHK-' + datetime.datetime.today().strftime('%d-%m-%Y')
    UPPER_ID_LIMIT = 5000
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
        os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    employmentAgenciesFDW = db[collectionName]

    count = 0

    for x in range(1, UPPER_ID_LIMIT): #UPPER_ID_LIMIT
        url = "http://www.eaa.labour.gov.hk/en/record.html?row-per-page=30&page-no=1&agency-id=" + str(x)
        while 1:
            try:
                page = requests.get(url)
                break
            except:
                time.sleep(60)
        contents = page.content
        soup = BeautifulSoup(contents, 'html.parser')

        if len(re.findall("We did not find this record", str(soup))) > 0:
            continue

        gov_id = str(x)

        results = soup.find_all("div", {"class" : "main container" })
        for result in results:
            if len(result) > 0:
                container_soup = result

        english_name = container_soup.find_all("h2", {"class" : "en-name" })
        if len(english_name) > 0:
            english_name = english_name[0].text
        else:
            english_name = ""

        chinese_name = container_soup.find_all("h2", {"class" : "chi-name" })
        if len(chinese_name) > 0:
            chinese_name = chinese_name[0].text
        else:
            chinese_name = ""

        p_tags = container_soup.find_all("p")

        valid_license_since = p_tags[1].text
        if valid_license_since is None:
            valid_license_since = ""

        district = p_tags[3].text
        if district is None:
            district = ""

        original_address = p_tags[5].text
        if original_address is None:
            original_address = ""

        telephone = p_tags[7].text
        if telephone is None:
            telephones = ""

        fax = p_tags[9].text
        if fax is None:
            fax = ""

        email = p_tags[11].text
        if email is None:
            email = ""

        placement_type = p_tags[13].text
        if placement_type is None:
            placement_type = ""

        lat = re.findall("lat: [0-9]+.[0-9]+", str(soup))[0]
        lng = re.findall("lng: [0-9]+.[0-9]+", str(soup))[0]

        if 'Foreign Domestic Helpers' not in placement_type:
            continue
        else:
            print(gov_id)
            print(english_name)
            print(count)
            agency_data= {"_id": gov_id,
                          "original_address": original_address,
                          "fax": fax,
                          "valid_license_since": valid_license_since,
                          "district": district,
                          "chinese_name": chinese_name,
                          "telephone": telephone,
                          "placement_type": placement_type,
                          "longitude": lng,
                          "english_name": english_name,
                          "latitude": lat,
                          "email": email}
            employmentAgenciesFDW.update({'_id': gov_id}, {'$set':agency_data}, upsert=True)
            count += 1

if __name__ == "__main__":
    main()
