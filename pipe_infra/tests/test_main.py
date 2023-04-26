"""
create test cases for ./src/App_code/pipeline.py using pytest   
"""
import sys

sys.path.append("/Users/bediako/Desktop/Data_engineering/pipe_infra/src")
import datetime

import psycopg2

from App_code.pipeline import (
    _get_exchange_insert_query,
    get_exchange_data,
    get_utc_from_unix_time,
    run,
)
from App_code.utils.config import get_warehouse_creds
from App_code.utils.db import WarehouseConnection


class TestPipeline:
    def test_get_utc_from_unix_time(self) -> None:
        ut: int = 1625249025588
        expected_dt = datetime.datetime(2021, 7, 2, 18, 3, 45, 588000)
        assert expected_dt == get_utc_from_unix_time(ut)

    def test_get_exchange_data(self):
        pass

    def test_get_exchange_insert_query(self):
        pass
