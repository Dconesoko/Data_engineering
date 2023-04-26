"""
Defining and creating schema

"""

from yoyo import step

__depends__ = {}

steps = [step("CREATE SCHEMA bitcoin", "DROP SCHEMA bitcoin CASCADE")]
