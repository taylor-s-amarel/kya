from pymongo import MongoClient
import re
import datetime
import os
import time

import codecs
import requests
from bs4 import BeautifulSoup

def print_agencies(text_file, collectionName):
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    phAgencies = db[collectionName]

    allAgencies = phAgencies.find({})

    for i, agency in enumerate(allAgencies):
        print(i)

        _id = agency['_id']

        name = agency['name']
        if name is None:
            name = ''

        address = agency['address']
        if address is None:
            address = ''

        license_start_date = agency['license_start_date']
        if license_start_date is None:
            license_start_date = ''

        license_end_date = agency['license_end_date']
        if license_end_date is None:
            license_end_date = ''

        representative = agency['representative']
        if representative is None:
            representative = ''

        status = agency['status']
        if status is None:
            status = ''

        website = agency['website']
        if website is None:
            website = ''

        email = agency['email']
        if email is None:
            email = ''

        telephones = agency['telephone']
        if telephones is None:
            telephones = ''
        else:
            telephones = ','.join(telephones)

        main_line = _id + "|" + name + "|" +  address + "|" + license_start_date + "|" + license_end_date + "|" + representative + "|" + status + "|" + website + "|" + email + "|" + telephones
        text_file.write(main_line)
        text_file.write("\n")

def main():
    timestamp = datetime.datetime.today().strftime('%d-%m-%Y')
    timestamp = '09-11-2018'
    collectionName = 'employmentAgenciesPH-' + timestamp
    if not os.path.exists('./archive/' + collectionName):
        os.makedirs('./archive/' + collectionName)
    path = './archive/'+ collectionName + '/agencies.csv'
    text_file = codecs.open(path, "a", encoding="utf-8")
    text_file.write(u"_id|name|address|license_start_date|license_end_date|representative|status|website|email|telephones")
    text_file.write("\n")
    print_agencies(text_file, collectionName)

if __name__ == "__main__":
    main()
