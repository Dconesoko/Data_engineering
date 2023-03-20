from yoyo import get_backend,read_migrations
import sys
from dotenv import load_dotenv
load_dotenv()

from App_code.utils import config
from App_code.utils.db import WarehouseConnection,DBConnection

con_data:DBConnection = config.get_warehouse_creds()
con_str:str = WarehouseConnection(con_data).conn_url

migrations=read_migrations("./migrations")
backend=get_backend(con_str)

with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))
    print("done applying migrations")
