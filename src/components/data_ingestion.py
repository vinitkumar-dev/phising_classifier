from src.exception import CustomEXception
from src.constant import *
from src.logger import logging
from src.utils.main_utils import MainUtils

from dataclasses import dataclass

import os,sys
import numpy as np
import pandas as pd

from pymongo import MongoClient

@dataclass
class DataIngestionConfig:
    artifact_folder:str = os.path.join(ARTIFACTS_DIR)


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()


    def export_collection_as_dataframe(self,collection_name,db_name):

       try: 
            mongo_client = MongoClient(MONGO_DB_URL)
            collection = mongo_client[db_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns:
                df = df.drop('_id',axis=1,inplace=True)

            df.replace('na',np.nan,inplace=True)

            return df


       except Exception as e:
           raise CustomEXception()
    
    def export_data_into_feature_store_file_path(self):

        try:

            logging.info('Exporting data from mongodb')
            
            raw_file_path  = self.data_ingestion_config.artifact_folder
            os.makedirs(raw_file_path,exist_ok=True)

            phishing_data = self.export_collection_as_dataframe(collection_name=MONGO_DATABASE_NAME,db_name=MONGO_DATABASE_NAME)

            logging.info(f'saving exported data into feature store file path :{raw_file_path}')

            feature_store_file_path = os.path.join(raw_file_path,'phishing.csv')

            phishing_data.to_csv(feature_store_file_path,index=False)

            return feature_store_file_path


        except Exception as e:
            raise CustomEXception(e,sys)
        
    
    def initiate_data_ingestion(self):

        try:
            logging.info('Entered initiated_Data_ingestion method of data_integration class')

            feature_store_file_path = self.export_data_into_feature_store_file_path()

            logging.info('got the data from  mongodb')
            logging.info('exited initiate_data_ingestion methods od data ingestion class')

            return feature_store_file_path


        except Exception as e:
            raise CustomEXception(e,sys)
            
