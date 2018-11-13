import os
import pandas as pd
from urllib.request import urlretrieve

# Get the DATA into local filesystem
# https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k
URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

"""
Function get_myFreemontData
Param1 : url
Param2 : filename
Returns: data set
"""

def get_myFreemontData(url=URL, filename='mycsv.csv'):
    if not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('mycsv.csv', index_col='Date', parse_dates=True)
    # Add columns shorter header
    data.columns=['West','East']
    # Add a Total column
    data['Total'] = data['West']+data['East']
    return data