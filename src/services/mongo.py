from pymongo import MongoClient

from ..env import TEST_DATABASE

test = MongoClient(TEST_DATABASE).get_default_database()
