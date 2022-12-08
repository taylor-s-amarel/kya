import agency_agency_address_text_compare
import agency_agency_email
import agency_agency_exact_address
import agency_agency_fax
import agency_agency_telephone
import agency_money_lender_address_text_compare
import agency_money_lender_exact_address

"""
Purpose:
    Run this file to run all the different components of our preprocessing
    Make sure that you have your app-env and venv set up beforehand
"""

def main():
    timestamp = '06-04-2019'

    print('Agency agency address text compare')
    print('')
    print('')
    agency_agency_address_text_compare.execute(timestamp)

    print('Agency agency email')
    print('')
    print('')
    agency_agency_email.execute(timestamp)

    print('Agency agency exact address')
    print('')
    print('')
    agency_agency_exact_address.execute(timestamp)

    print('Agency agency fax')
    print('')
    print('')
    agency_agency_fax.execute(timestamp)

    print('Agency agency telephone')
    print('')
    print('')
    agency_agency_telephone.execute(timestamp)

    print('Agency money lender address text compare')
    print('')
    print('')
    agency_money_lender_address_text_compare.execute(timestamp)


    print('Agency money lender exact address')
    print('')
    print('')
    agency_money_lender_exact_address.execute(timestamp)

if __name__ == '__main__':
	main()
