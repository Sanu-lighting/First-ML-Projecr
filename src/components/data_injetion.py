import os
import sys
from src.exception import CustomeException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataInjetionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")
class DataInjection:
    def __init__(self):
        self.injection_config=DataInjetionConfig()
    def Inititiate_data_injetion(self):
        logging.info("Enter the Data Injetion method or component: ")
        try:
            df=pd.read_csv('Notebooks/data/StudentsPerformance.csv')
            logging.info("Read The data set as dataframe")
            os.makedirs(os.path.dirname(self.injection_config.train_data_path),exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.injection_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injection_config.test_data_path,index=False,header=True)
            logging.info("Injetion of the data is completed")
            return(
                self.injection_config.train_data_path,
                self.injection_config.test_data_path
            )
        except Exception as e:
            raise CustomeException(e,sys)
        

if __name__=="__main__":
    obj=DataInjection()
    obj.Inititiate_data_injetion()

        

