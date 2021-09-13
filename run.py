import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures input from the user
    """
    print('Please enter sales data from the last market')
    print('Data should be six nubmer, separated by commas')
    print('Example: 10,20,30,40,50,60\n')

    data_str = input('Enter your data here: ')
    
    sales_data = data_str.split(',')
    validate_data(sales_data)

def validate_data(values):
    """
    Check for the correct formatting being inserted by the user and raise error if not
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 value required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')

get_sales_data()