from pymongo import MongoClient
import datetime
import os
import csv
import codecs

def print_agency_agency_exact_address(text_file, collectionName):
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    hkAgencies = db[collectionName]

    allAgencies = hkAgencies.find({})

    for i, agency in enumerate(allAgencies):
        print(i)
        similarAgencies = agency["sharedAddressExactAgencies"]
        if(len(similarAgencies) == 0):
            continue
        main_line = agency["_id"] + "|" + agency["english_name"] + "|" + agency["original_address"] + "\n"
        text_file.write(main_line)
        for similarAgencyId in similarAgencies:
            similarAgency = hkAgencies.find_one({"_id": similarAgencyId})
            sub_line = similarAgency["_id"] + "|" + similarAgency["english_name"] + "|" + agency["original_address"] + "\n"
            text_file.write(sub_line)
        text_file.write("\n")

def execute(timestamp):
    collectionName = 'employmentAgenciesHK-' + timestamp
    if not os.path.exists('./archive/' + collectionName):
        os.makedirs('./archive/' + collectionName)
    path = './archive/' + collectionName + '/agency_agency_exact_address.csv'
    text_file = codecs.open(path, "a", encoding="utf-8")
    text_file.write(u"govid|english_name|address" + "\n")
    text_file.write("\n")
    print_agency_agency_exact_address(text_file, collectionName)
