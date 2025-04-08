from src.component.data_transformation import DataTransformations
import numpy as np


def test_initiate_data_transformation():
    data_transformation = DataTransformations(folder_name='test_folder')
    tr_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path=r"test_folder/train.csv",test_path=r'test_folder/test.csv')
    assert isinstance(tr_arr, np.ndarray)
    assert isinstance(test_arr,np.ndarray)


if __name__ == '__main__':
    test_initiate_data_transformation()