import os
import sys
import dotenv

dotenv.load_dotenv()

from App_code.utils.db import DBConnection


def get_warehouse_creds() -> DBConnection:
    return DBConnection (
        user=os.getenv('WAREHOUSE_USER') or  os.getenv("POSTGRES_USER"),
        password=os.getenv('WAREHOUSE_PASSWORD') or os.getenv("POSTGRES_PASSWORD"),
        db=os.getenv('WAREHOUSE_DB') or os.getenv("POSTGRES_DB"),
        host="warehouse",
        port=int(os.getenv('WAREHOUSE_PORT', 5432))
    )
