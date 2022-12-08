import requests
import json
import codecs
from pymongo import MongoClient
import os
import datetime


"""
Purpose:
    Scrapes down information on Money Lending Agencies from the Customs and Excise
    Department's Money Service Operators Licensing System's Website.

Returns:
    A csv file with the following Fields
        address
        chinese_name
        english_name

How does it work:
    We query the Department's db for every Money Service Operator, which returns
    roughly 200 page worth of agencies (about 10 per page). We then access the content
    of these pages as json objects, from which we extract our relevant values.
    These values are written to a csv file.

Runtime:
    A few minutes. Makes about 200 requests


"""

def main():
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
        os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    collectionName = 'moneyLendersHK-' + datetime.datetime.today().strftime('%d-%m-%Y')
    moneyLenders = db[collectionName]

    session = requests.Session()
    session.cookies.get_dict()
    response = session.get('https://eservices.customs.gov.hk/MSOS/wsrh/001s1?searchBy=ALL')

    ind=1

    while True:
        url = "https://eservices.customs.gov.hk/MSOS/wsrh/loadSearchLicenseGrid?_search=false&nd=1518672577767&rows=10&page="+ str(ind) + "&sidx=coNameChn&sord=asc"
        page = session.get(url)
        contents = json.loads(page.content.decode('utf-8'))
        search_list = contents["pubSrchList"]

        #Checks to see if we have reached the end of the records
        if search_list is None:
            break

        print(ind)
        for lender in search_list:
            english_name = lender["coName"]
            chinese_name = lender["coNameChn"]
            address = lender["fullAddress"]

            if english_name is None or len(english_name) == 0:
                english_name = ""

            if chinese_name is None or len(chinese_name) == 0:
                chinese_name = ""

            if address is None or len(address) == 0:
                address = ""

            lender_data={'english_name':english_name,'chinese_name':chinese_name,'address':address}
            moneyLenders.update({'english_name':english_name,'address':address},{'$set':lender_data}, upsert=True)

        ind += 1

if __name__ == "__main__":
    main()
