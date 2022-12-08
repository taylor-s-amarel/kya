from pymongo import MongoClient
import os
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
        address = agency['original_address']
        gov_id = agency['_id']
        if len(address) > 1:
            matches = hkAgencies.find({"$and":[{"original_address": address},
                                                {"_id":{'$ne':gov_id}}]})
            matching_ids = [str(some_agency["_id"]) for some_agency in matches]
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedAddressExactAgencies": list(matching_ids)}})
        else:
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedAddressExactAgencies": []}})
        count+=1
        if count%20==0:
            print count
