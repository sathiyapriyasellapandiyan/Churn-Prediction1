from src.logger import logging
import os
import sys
from sklearn.model_selection import train_test_split
import pandas as pd
from src.exception import CustomException
from src.component.model_trainer import ModelTrainer 
from src.component.data_transformation import DataTransformations

class DataIngestionConfig:
    def __init__(self, folder_name="artifacts"):
        self.folder_name = folder_name
        self.train_data_path: str = os.path.join(self.folder_name, "train.csv")
        self.test_data_path: str = os.path.join(self.folder_name, "test.csv")
        self.raw_data_path: str = os.path.join(self.folder_name, "raw.csv")

class DataIngestion:
    def __init__(self,folder_name="artifacts"):
        self.ingestion_config = DataIngestionConfig(folder_name)

    def intiate_data_ingestion(self,path):
        logging.info("DataIngestion gets started ...")
        try:
            df = pd.read_csv(path)
            # log,ging.info("Data has been readed from the source.")
            # os.makedirs(os.path.join(self.ingestion_config.train_data_path))
            # os.makedirs(os.path.join(self.ingestion_config.test_data_path))
            # os.makedirs(os.path.join(self.ingestion_config.raw_data_path))
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_data, test_data = train_test_split(df,test_size=.3,random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Train and test data has been splited and saved in their directory ...")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_path,test_path = data_ingestion.intiate_data_ingestion(path="artifacts\customer_churn.csv")
    data_transformation = DataTransformations()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path,test_path)
    model_trainer = ModelTrainer()
    report = model_trainer.intiate_model_trainer(train_arr,test_arr)
    print("Classification Report :")
    print(report)