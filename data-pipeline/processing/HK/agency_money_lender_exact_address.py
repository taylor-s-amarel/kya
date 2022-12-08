from pymongo import MongoClient
from pymongo import TEXT
import os
import csv
import datetime

def execute(timestamp):
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    collectionName = 'employmentAgenciesHK-' + timestamp
    hkAgencies = db[collectionName]

    #if hkAgencies is empty then we haven't scraped yet, so we can't do any processing.
    count = hkAgencies.count({})
    if count == 0:
        print("{}, has not yet been scraped".format(collectionName))
        return

    moneyLenderCollectionName = 'moneyLendersHK-' + timestamp
    moneyLenders = db[moneyLenderCollectionName]

    if len(moneyLenders.index_information()) < 2:
        moneyLenders.create_index([('address', TEXT)], default_language='english');
        print("address_text index created")

    allAgencies = hkAgencies.find({})
    count=0

    for agency in allAgencies:
        address = agency['original_address']
        gov_id = agency['_id']
        english_name = agency['english_name']

        if len(address) > 1:
            address = address.upper()
            matches = moneyLenders.find({"address": address})
            matching_ids = [some_agency["_id"] for some_agency in matches]
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedAddressExactMoneyLenders": list(matching_ids)}})
        else:
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedAddressExactMoneyLenders": []}})

        count+=1
        if count%20==0:
            print count
