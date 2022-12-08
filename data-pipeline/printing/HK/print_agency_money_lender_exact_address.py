from pymongo import MongoClient
import datetime
import os
import csv
import codecs

def print_agency_money_lender_exact_address(text_file, collectionName, moneyLenderCollectionName):
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    hkAgencies = db[collectionName]
    moneyLenders = db[moneyLenderCollectionName]

    allAgencies = hkAgencies.find({})

    for i, agency in enumerate(allAgencies):
        print(i)
        exactMoneyLenders = agency["sharedAddressExactMoneyLenders"]
        if(len(exactMoneyLenders) == 0):
            continue
        main_line = agency["_id"] + "|" + agency["english_name"] + "|" + agency["original_address"] + "\n"
        text_file.write(main_line)
        for exactMoneyLenderId in exactMoneyLenders:
            exactMoneyLender = moneyLenders.find_one({"_id": exactMoneyLenderId})
            sub_line = str(exactMoneyLender["_id"]) + "|" + exactMoneyLender["english_name"] + "|" + exactMoneyLender["address"] + "\n"
            text_file.write(sub_line)
        text_file.write("\n")

def execute(timestamp):
    collectionName = 'employmentAgenciesHK-' + timestamp
    moneyLenderCollectionName = 'moneyLendersHK-' + timestamp
    if not os.path.exists('./archive/' + collectionName):
        os.makedirs('./archive/' + collectionName)
    path = './archive/' + collectionName + '/agency_money_lender_exact_address.csv'
    text_file = codecs.open(path, "a", encoding="utf-8")
    text_file.write(u"govid|english_name|address" + "\n")
    text_file.write("\n")
    print_agency_money_lender_exact_address(text_file, collectionName, moneyLenderCollectionName)
