import os
import pytest
import pandas as pd
from src.component.data_ingestion import DataIngestion

folder_name = 'test_folder'
os.makedirs(folder_name,exist_ok=True)
@pytest.fixture
def setup_data_ingestion():
    dic = {
        'ids':['adb323','bed432'],
        'gender':['male','female']
    }
    df = pd.DataFrame(dic)
    df.to_csv(os.path.join(folder_name,'churn.csv'),index=False)
    yield folder_name

def test_intiate_data_ingestion(setup_data_ingestion):
    data_ingestion = DataIngestion(setup_data_ingestion)
    tr_path,te_path = data_ingestion.intiate_data_ingestion(path=os.path.join(folder_name,'churn.csv'))
    assert os.path.exists(tr_path)
    assert os.path.exists(te_path)
    
if __name__ == '__main__':
    test_intiate_data_ingestion()
    os.rmdir(folder_name)