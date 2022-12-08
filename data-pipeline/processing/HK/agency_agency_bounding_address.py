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
    count = 0

    for agency in allAgencies:
        address = agency['original_address']
        gov_id = agency['_id']
        lat = agency['latitude']
        lng = agency['longitude']
        E=.00001
        if lat not None and lng not None and len(address) > 1:
            matches = hkAgencies.find({"$and":[{"latitude": {"$gt": lat-E, "$lt": lat+E}}, \
                                                {"longitude":  {"$gt": lng - E, "$lt": lng + E}}]})
            matching_ids = [str(some_agency["_id"]) for some_agency in matches]
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedAddressBoundingBoxAgencies": list(matching_ids)}})
        else:
            hkAgencies.update({"_id":gov_id}, {"$set": {"sharedAddressBoundingBoxAgencies": []}})
        count+=1
        if count%20==0:
            print count
