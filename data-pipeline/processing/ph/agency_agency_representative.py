from pymongo import MongoClient
import os
import csv
import datetime

def main():
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    collectionName = 'employmentAgenciesPH-' + datetime.datetime.today().strftime('%d-%m-%Y')
    collectionName = 'employmentAgenciesPH-25-12-2018'
    phAgencies = db[collectionName]

    #if phAgencies is empty then we haven't scraped yet, so we can't do any processing.
    count = phAgencies.count({})
    if count == 0:
        print("{}, has not yet been scraped".format(collectionName))
        return
    allAgencies = phAgencies.find({})
    count=0
    for agency in allAgencies:
        _id = agency['_id']
        representative = agency['representative']
        if len(representative) > 0:
            matches = phAgencies.find({ "$and": [{"representative": representative},{"_id":{'$ne':_id}}]})
            matching_ids = [str(some_agency["_id"]) for some_agency in matches]
            phAgencies.update({"_id":_id}, {"$set": {"sharedRepresentativeAgencies": list(matching_ids)}})
        else:
            phAgencies.update({"_id":_id}, {"$set": {"sharedRepresentativeAgencies": []}})
        count += 1
        if count % 20 == 0:
            print count

if __name__ == '__main__':
    main()
