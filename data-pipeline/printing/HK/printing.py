"""
Purpose:
    Run this script to create CSVs which will contain old versions of our
    employmentAgenciesFDW and moneyLenders collections
"""

import print_agencies
import print_agency_agency_email
import print_agency_agency_exact_address
import print_agency_agency_fax
import print_agency_agency_similar_address
import print_agency_agency_telephone
import print_agency_flags
import print_agency_money_lender_exact_address
import print_agency_money_lender_similar_address
import print_money_lenders

def main():
    timestamp = '06-04-2019'

    print('Print agencies')
    print('')
    print('')
    print_agencies.execute(timestamp)

    print('Print agency agency email')
    print('')
    print('')
    print_agency_agency_email.execute(timestamp)

    print('Print agency agency exact address')
    print('')
    print('')
    print_agency_agency_exact_address.execute(timestamp)

    print('Print agency agency fax')
    print('')
    print('')
    print_agency_agency_fax.execute(timestamp)

    print('Print agency agency similar address')
    print('')
    print('')
    print_agency_agency_similar_address.execute(timestamp)

    print('Print agency agency telephone')
    print('')
    print('')
    print_agency_agency_telephone.execute(timestamp)

    print('Print agency flags')
    print('')
    print('')
    print_agency_flags.execute(timestamp)

    print('Print agency money lender similar address')
    print('')
    print('')
    print_agency_money_lender_similar_address.execute(timestamp)

    print('Print agency money lender exact address')
    print('')
    print('')
    print_agency_money_lender_exact_address.execute(timestamp)

    print('Print money lenders')
    print('')
    print('')
    print_money_lenders.execute(timestamp)

if __name__ == '__main__':
    main()
