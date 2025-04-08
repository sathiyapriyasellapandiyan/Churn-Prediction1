from dataclasses import dataclass
import os
import sys
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    def __init__(self, folder_name="artifacts"):
        self.folder_name = folder_name
        self.preprocessor_file_obj : str = os.path.join(folder_name,'preprocessor.joblib')



class DataTransformations:
    def __init__(self,folder_name="artifacts"):
        self.transformation_config = DataTransformationConfig(folder_name)

    def get_data_transformer_object(self,data):
        try:
            num_cols = data.select_dtypes(['int','float']).columns.tolist()
            cat_cols = data.select_dtypes(['object','category']).columns[1:-1].tolist()
            # print(target_col,cat_cols)
            if 'churn' in num_cols:
                num_cols.remove('churn')
            if 'churn' in num_cols:
                num_cols.remove('churn')
            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='mean')),
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OrdinalEncoder()),
                    ('target',StandardScaler())
                ]
            )
            # target_pipeline = Pipeline(
            #     steps=[
            #         ('imputer',SimpleImputer(strategy='most_frequent')),
            #         ('encoder',OrdinalEncoder())
            #     ]
            # )
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline',num_pipeline,num_cols),
                    ('cat_pipeline',cat_pipeline,cat_cols)
                ]
            )
            logging.info("Preprocessor has been created ...")
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try : 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            chur_tr = train_df.iloc[:,-1]
            chur_te = test_df.iloc[:,-1]
            logging.info("Train and test data has been readed .")
            preprocessing_obj = self.get_data_transformer_object(train_df)
            print(train_df.head())
            print(test_df.head())
            print('\n columns',test_df.columns)
            train_arr = preprocessing_obj.fit_transform(train_df.iloc[:,1:])
            test_arr = preprocessing_obj.transform(test_df.iloc[:,1:])
            train_arr = np.c_[train_arr,chur_tr.values]
            test_arr = np.c_[test_arr,chur_te.values]
            save_object(
                filepath = self.transformation_config.preprocessor_file_obj,
                obj = preprocessing_obj
            )
            logging.info("Data has been transformed and saved in the source ...")
            return (
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_file_obj
            )
        except Exception as e:
            raise CustomException(e,sys)