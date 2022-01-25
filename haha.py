import urllib.request

print('Beginning file download with urllib2...')

url='https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv'


urllib.request.urlretrieve(url,'C://Users//Sai//Desktop//DataEngineer_Course//download.csv')
