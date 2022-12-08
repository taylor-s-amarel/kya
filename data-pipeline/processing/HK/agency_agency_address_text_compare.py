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

    if len(hkAgencies.index_information()) < 2:
        hkAgencies.create_index([('original_address', TEXT)], default_language='english');
        print("original_address_text index created")

    count = 0
    for agency in hkAgencies.find({}):
        address = agency['original_address']
        gov_id = agency['_id']
        if len(address) > 1:
            matches = hkAgencies.find(
                {
                    "$text": {'$search':address, '$caseSensitive': False},
                    '_id' : {'$ne':gov_id},
                    'original_address': {'$ne':address}
                },
                {'score': {'$meta': "textScore"}}
            )
            matches.sort([('score', {'$meta': 'textScore'})])
            above_threshold = []
            for match in matches:
                if match['score'] > 5 and match_floors(match['original_address'], address):
                    above_threshold.append(match['_id'])
            hkAgencies.update({"_id":gov_id}, {"$set": {"addressTextSimilarityAgencies": list(above_threshold)}})
        else:
            hkAgencies.update({"_id":gov_id}, {"$set": {"addressTextSimilarityAgencies": []}})
        count+=1
        if count%20==0:
            print count
