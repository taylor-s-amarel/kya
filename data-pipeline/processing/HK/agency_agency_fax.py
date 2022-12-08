from pymongo import MongoClient
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

    allAgencies = hkAgencies.find({})
    count=0

    for agency in allAgencies:
        fax = agency['fax']
        gov_id = agency['_id']
        if len(fax) > 1: #empty phone has length 1 in DB.
            matches = hkAgencies.find({"$and":[{"fax": fax}, {"_id":{'$ne':gov_id}}]})
            matching_ids = [str(some_agency["_id"]) for some_agency in matches]
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedFaxAgencies": list(matching_ids)}})
        else:
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedFaxAgencies": []}})
        count+=1
        if count%20==0:
            print count
