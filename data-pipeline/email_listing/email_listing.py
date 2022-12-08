"""
Purpose:
    Access the json file at /src/data/allAgencies.json and prints out the emails of all
    accredited agencies
"""

import os
import json

ALL_AGENCIES_JSON_FILE_NAME = 'allAgencies.json'


def main():
    path = os.path.join('..', '..', 'client', 'src', 'data', ALL_AGENCIES_JSON_FILE_NAME)
    with open(path) as json_file:  
        data = json.load(json_file)
        for eaaId in data:
            agency_details = data[eaaId]
            if agency_details['isAccredited'] and 'email' in agency_details:
                email = agency_details['email'].rstrip()
                if len(email) > 0:
                    print(email)

if __name__ == '__main__':
    main()
