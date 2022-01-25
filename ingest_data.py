import pandas as pd
from sqlalchemy import create_engine
import time
import urllib.request
import argparse


def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url=params.url
    
    csv_name='output.csv'
    ddd='https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv'
    
    urllib.request.urlretrieve(ddd,csv_name)
    
    #download the csv
    
    engine=create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    engine.connect()

    #df = pd.read_csv('yellow_tripdata_2021-01.csv',nrows=100)
    #print(pd.io.sql.get_schema(df,name='yello_taxi_data',con=engine))


    # In[7]:


    df_ite=pd.read_csv(csv_name,iterator=True,chunksize=100000)


    # In[8]:


    df=next(df_ite)
    
    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
    
    df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')


    df.to_sql(name=table_name,con=engine,if_exists='append')


    # In[17]:



    while True:
        t_s=time.time()
        df=next(df_ite)
        df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name,con=engine,if_exists='append')
        t_e=time.time()
        print('insereted another chuk of ..took %.3f second'%(t_e-t_s))




if __name__=='__main__':


    parser = argparse.ArgumentParser(description='ingest to postgre')

    parser.add_argument('--user',help='user name for posttgres')
    parser.add_argument('--password',help='password name for posttgres')
    parser.add_argument('--host',help='host name for posttgres')
    parser.add_argument('--port',help='port name for posttgres')
    parser.add_argument('--db',help='db name for posttgres')
    parser.add_argument('--table_name',help='table_name to write results into')
    parser.add_argument('--url',help='url of csv')


    args = parser.parse_args()
    
    main(args)

