"""
Defining and creating schema

"""
from typing import Dict

from yoyo import step

__depends__: Dict[str, str] = {}

steps = [step("CREATE SCHEMA bitcoin", "DROP SCHEMA bitcoin CASCADE")]
