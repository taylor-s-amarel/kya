from pymongo import MongoClient
import datetime
import os
import csv
import codecs

def print_agency_flags(text_file, collectionName):
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    hkAgencies = db[collectionName]

    allAgencies = hkAgencies.find({})

    for i, agency in enumerate(allAgencies):
        print(i)
        flags = []
        exactAddressAgencies = agency["sharedAddressExactAgencies"]
        if(len(exactAddressAgencies) > 0):
            flags.append('exact agency address')
        similarAddressAgencies = agency["addressTextSimilarityAgencies"]
        if(len(similarAddressAgencies) > 0):
            flags.append('similar agency address')
        sharedTelephoneAgencies = agency["sharedPhoneAgencies"]
        if(len(sharedTelephoneAgencies) > 0):
            flags.append('similar agency telephone')
        sharedFaxAgencies = agency["sharedFaxAgencies"]
        if(len(sharedFaxAgencies) > 0):
            flags.append('similar agency fax')
        sharedEmailAgencies = agency["sharedEmailAgencies"]
        if(len(sharedEmailAgencies) > 0):
            flags.append('similar agency email')
        sharedExactAddressMoneyLenders = agency["sharedAddressExactMoneyLenders"]
        if(len(sharedExactAddressMoneyLenders) > 0):
            flags.append('exact money lender address')
        sharedSimilarAddressMoneyLenders = agency["addressTextSimilarityMoneyLenders"]
        if(len(sharedSimilarAddressMoneyLenders) > 0):
            flags.append('similar money lender address')

        if(len(flags) > 0):
            main_line = agency["_id"] + "|" + agency["english_name"] + "|" + ','.join(flags) + "\n"
            text_file.write(main_line)

def execute(timestamp):
    collectionName = 'employmentAgenciesHK-' + timestamp
    if not os.path.exists('./archive/' + collectionName):
        os.makedirs('./archive/' + collectionName)
    path = './archive/' + collectionName + '/agency_flags.csv'
    text_file = codecs.open(path, "a", encoding="utf-8")
    text_file.write(u"govid|english_name|flags" + "\n")
    text_file.write("\n")
    print_agency_flags(text_file, collectionName)
