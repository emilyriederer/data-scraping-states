# data from: https://dl.ncsbe.gov/?prefix=ENRS/2020_11_03/

import urllib.request
url = 'https://s3.amazonaws.com/dl.ncsbe.gov/ENRS/2020_11_03/absentee_counts_county_20201103.csv'
urllib.request.urlretrieve(url, 'data/nc.csv')