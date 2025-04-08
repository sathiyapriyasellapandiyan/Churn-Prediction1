import os
import joblib
from src.exception import CustomException
import sys


def save_object(filepath,obj):
    try : 
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        joblib.dump(obj,filepath)

    except Exception as e:
        raise CustomException(e,sys)