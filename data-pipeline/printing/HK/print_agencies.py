'''
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
    Roughly 50 Minutes

Note:
    CSV Files will be stored in the folder "archive". Each time this script runs
    it will create a new subfolder within archive. This subfolder will be titled
    to signify its creation date.

'''
#An arbitrary number above however many registered agencies there are.
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
    hkAgencies = db[collectionName]

    allAgencies = hkAgencies.find({})

    for i, agency in enumerate(allAgencies):
        print(i)

        _id = agency['_id']

        english_name = agency['english_name']
        if english_name is None:
            english_name = ''

        chinese_name = agency['chinese_name']
        if chinese_name is None:
            chinese_name = ''

        address = agency['original_address']
        if address is None:
            address = ''

        district = agency['district']
        if district is None:
            district = ''

        latitude = agency['latitude']
        if latitude is None:
            latitude = ''

        longitude = agency['longitude']
        if longitude is None:
            longitude = ''

        email = agency['email']
        if email is None:
            email = ''

        telephone = agency['telephone']
        if telephone is None:
            telephone = ''

        fax = agency['fax']
        if fax is None:
            fax = ''

        placement_type = agency['placement_type']
        if placement_type is None:
            placement_type = ''

        valid_license_since = agency['valid_license_since']
        if valid_license_since is None:
            valid_license_since = ''

        main_line = _id + "|" + english_name + "|" + chinese_name + "|" + address + "|" + district + "|" + str(latitude) + "|" + str(longitude) + "|" + email + "|" + telephone + "|" + fax + "|" + placement_type + "|" + str(valid_license_since)
        text_file.write(main_line)
        text_file.write("\n")

def execute(timestamp):
    collectionName = 'employmentAgenciesHK-' + timestamp
    if not os.path.exists('./archive/' + collectionName):
        os.makedirs('./archive/' + collectionName)
    path = './archive/'+ collectionName + '/agencies.csv'
    text_file = codecs.open(path, "a", encoding="utf-8")
    text_file.write(u"gov_id|english_name|chinese_name,address|district|latitude|longitude|email|telephone|fax|placement_type|valid_license_since" + "\n")
    print_agencies(text_file, collectionName)
