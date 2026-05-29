import os,yaml,sys,pickle

from src.exception import CustomException
from src.logger import logging
from src.constant import *

class MainUtils:

    def read_yaml_file(self,filename:str)->dict:
        try:
            with open(filename,'rb') as yaml_file:
                return yaml.safe_load(yaml_file)
            
        except Exception as e:
            raise CustomException(e,sys)

    def read_schema_config_file(self):
        try:
            schema_config = self.read_yaml_file(os.path.join('config','schema.yaml'))

            return schema_config

        except Exception as e:
            raise CustomException(e,sys)

    
    @staticmethod
    def save_object(file_path:str,obj:object):
        logging.info('Entered the save_object method of MainUtils class')

        try:
            with open(file_path,'wb') as file_obj:
                pickle.dump(obj,file_obj)

            logging.info('Exited the save_object method of MainUtils class')

        except Exception as e:
            raise CustomException(e, sys) from e
        
    @staticmethod
    def load_object(file_path:str):
        logging.info('Entered the load_object method of MainUtils class')

        try:
            with open(file_path,'rb') as file_obj:
               obj = pickle.load(file_obj)

               logging.info('Exited the save_object method of MainUtils class')
               return obj  
                  
        except Exception as e:
            raise CustomException(e, sys) from e
