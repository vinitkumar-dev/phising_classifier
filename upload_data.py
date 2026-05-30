import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from src.constant import *



client = MongoClient(MONGO_DB_URL)

df = pd.read_csv('notebooks/phising.csv')

json_record = list(json.loads(df.T.to_json()).values())

#is used to convert a Pandas DataFrame into a list of JSON-like records (row-wise dictionaries).

db = client[MONGO_DATABASE_NAME] # db create
coll_create= db[MONGO_COLLECTION_NAME] # table like

coll_create.insert_many(json_record)