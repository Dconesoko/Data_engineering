import sys

sys.path.append("/home/nanabediako/Desktop/Data Engineering/pipe_infra/src")


import datetime
import os
import typing as typ

from pytest import fixture

from App_code.pipeline import (
    _get_exchange_insert_query,
    get_exchange_data,
    get_utc_from_unix_time,
)
from App_code.utils.db import WarehouseConnection


class TestPipeline:
    def test_get_utc_from_unix_time(self):
        assert datetime.datetime(
            2021, 7, 2, 18, 3, 45, 588000
        ) == get_utc_from_unix_time(1625249025588)

    def test_get_exchange_data(self):
        assert get_exchange_data() != []
