"""
create test cases for ./src/App_code/pipeline.py using pytest   
"""
import sys
sys.path.append("/Users/bediako/Desktop/Data_engineering/pipe_infra/src")
import psycopg2
import datetime
from App_code.pipeline import get_utc_from_unix_time,run,get_exchange_data,_get_exchange_insert_query
from App_code.utils.db import WarehouseConnection
from App_code.utils.config import get_warehouse_creds

class TestPipeline:
    def test_get_utc_from_unix_time(self)->None:
        ut: int = 1625249025588
        expected_dt = datetime.datetime(2021, 7, 2, 18, 3, 45, 588000)
        assert expected_dt == get_utc_from_unix_time(ut)

    def test_get_exchange_data(self):
        pass
    
    def test_get_exchange_insert_query(self):
        pass
