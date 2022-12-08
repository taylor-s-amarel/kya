from pymongo import MongoClient
from pymongo import TEXT
import os
import re
from match_floors import match_floors
import csv
import datetime

# {
#     "_id": "ff6c86ed71196c8101bf7f9011d4655d62a5b412",
#     "address": "3F NICFUR BLDG 1990 TAFT AVENUE COR QUIRINO AVE MALATE, MANILA",
#     "license_end_date": "2/6/2020",
#     "license_start_date": "2/6/2018",
#     "name": "1010 EPHESIANS HUMAN RESOURCES INC",
#     "representative": "RESANA L LACANARIA",
#     "status": "Valid License",
#     "telephone": [
#         "2967850",
#         "0927467",
#         "0947291"
#     ],
#     "website": ""
# }

def main():
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    collectionName = 'employmentAgenciesPH-' + datetime.datetime.today().strftime('%d-%m-%Y')
    phAgencies = db[collectionName]

    #if phAgencies is empty then we haven't scraped yet, so we can't do any processing.
    count = phAgencies.count({})
    if count == 0:
        print("{}, has not yet been scraped".format(collectionName))
        return

    if len(phAgencies.index_information()) < 2:
        phAgencies.create_index([('address', TEXT)], default_language='english');
        print("address_text index created")

    count = 0
    for agency in phAgencies.find({}):
        address = agency['address']
        _id = agency['_id']
        if len(address) > 0:
            matches = phAgencies.find(
                {
                    "$text": {'$search':address, '$caseSensitive': False},
                    '_id' : {'$ne':_id},
                    'address': {'$ne':address}
                },
                {'score': {'$meta': "textScore"}}
            )
            matches.sort([('score', {'$meta': 'textScore'})])
            above_threshold_ids = []
            above_threshold_names_and_addresses = []
            for match in matches:
                if match['score'] > 5:
                    above_threshold_ids.append(match['_id'])
                    above_threshold_names_and_addresses.append((match['name'], match['address']))
            phAgencies.update({"_id":_id}, {"$set": {"addressTextSimilarityAgencies": list(above_threshold_ids)}})
            print agency['name']
            print agency['address']
            print above_threshold_names_and_addresses
            print ""
        else:
            phAgencies.update({"_id":_id}, {"$set": {"addressTextSimilarityAgencies": []}})
        count += 1
        if count % 20 == 0:
            print count

if __name__ == '__main__':
    main()
