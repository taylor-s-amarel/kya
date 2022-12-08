from pymongo import MongoClient
from pymongo import TEXT
import os
import re
from match_floors import match_floors
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

    for agency in hkAgencies.find({}):
        address = agency['original_address']
        if len(address) > 1:
            agency_id = agency['_id']
            matches = moneyLenders.find(
                {"$text": {'$search': address,'$caseSensitive': False}},
                { 'score': { '$meta': "textScore" }}
            )
            matches.sort([('score', {'$meta': 'textScore'})])
            above_threshold=[]
            for match in matches:
                if match['score'] > 5 and match_floors(match['address'], address):
                    above_threshold.append(match['_id'])
            hkAgencies.update({"_id": agency_id}, {"$set": {"addressTextSimilarityMoneyLenders": list(above_threshold)}})
        else:
            hkAgencies.update({"_id": agency_id}, {"$set": {"addressTextSimilarityMoneyLenders": []}})
        count+=1
        if count%20==0:
            print count
