import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier
from src.exception import CustomException
from src.logger import logging 
from src.utils import save_object
from sklearn.metrics import classification_report

@dataclass
class ModelTrainerConfig:
    def __init__(self,folder_name='artifacts'):
        self.train_model_file_path :str = os.path.join(folder_name,'model.joblib')


class ModelTrainer:
    def __init__(self,folder_name='artifacts'):
        self.model_trainer_config = ModelTrainerConfig(folder_name)

    def intiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("model training has been started ...")
            x_train,x_test,y_train,y_test = (
                train_arr[:,:-1],test_arr[:,:-1],train_arr[:,-1],test_arr[:,-1]
            )
            model = RandomForestClassifier()
            model.fit(x_train,y_train)
            pred = model.predict(x_test)
            # print("Classification Report :")
            # print(classification_report(y_test,pred))
            save_object(
                filepath=self.model_trainer_config.train_model_file_path,
                obj = model
            )
            logging.info('model has been trained and saved in the source ...')
            return classification_report(y_test,pred)

        except Exception as e:
            return CustomException(e,sys)
