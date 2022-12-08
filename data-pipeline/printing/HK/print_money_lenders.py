'''
Purpose:
    Scrapes down information on Money Lending Agencies from the Customs and Excise
    Department's Money Service Operators Licensing System's Website.

Returns:
    A csv file with the following Fields
        english_name
        chinese_name
        address
    Note, rows will be in alphabetical order by english_name

How does it work:
    We query the Department's db for every Money Service Operator, which returns
    roughly 200 page worth of agencies (about 10 per page). We then access the content
    of these pages as json objects, from which we extract our relevant values.
    These values are written to a csv file.

Runtime:
    Runs in less than a minute
'''

from pymongo import MongoClient
import datetime
import codecs
import os

def print_money_lenders(text_file, collectionName):
    mongoUri = 'mongodb://' + os.environ.get('DATABASE_USERNAME') + ':' + \
                os.environ.get('DATABASE_PASSWORD') + '@ds249757.mlab.com:49757/help'
    client = MongoClient(mongoUri)
    db = client['help']
    moneyLenders = db[collectionName]

    allMoneyLenders = moneyLenders.find({})

    for i, moneyLender in enumerate(allMoneyLenders):
        _id = moneyLender['_id']
        english_name = moneyLender['english_name']
        chinese_name = moneyLender['chinese_name']
        address = moneyLender['address']
        if english_name is None:
            english_name = 'None'
        if chinese_name is None:
            chinese_name = 'None'
        if address is None:
            address = 'None'
        line = english_name + '|' + chinese_name + '|' + address + '\n'
        text_file.write(line)
        print(i)

def execute(timestamp):
    collectionName = 'moneyLendersHK-' + timestamp
    if not os.path.exists('./archive/'+ collectionName):
        os.makedirs('./archive/' + collectionName)
    path = './archive/' + collectionName + '/money_lenders.csv'
    text_file = codecs.open(path, 'a', encoding='utf-8')
    text_file.write('english_name|chinese_name|address' + '\n')
    print_money_lenders(text_file, collectionName)

if __name__ == '__main__':
    timestamp = '06-04-2019'
    execute(timestamp)
