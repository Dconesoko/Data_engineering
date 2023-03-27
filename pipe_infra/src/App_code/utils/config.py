import os
import sys

from App_code.utils.db import DBConnection


def get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv('WAREHOUSE_USER', ''),
        password=os.getenv('WAREHOUSE_PASSWORD', ''),
        db=os.getenv('WAREHOUSE_DB', ''),
        host="172.19.0.3",
        port=int(os.getenv('WAREHOUSE_PORT', 5432)),
    )
