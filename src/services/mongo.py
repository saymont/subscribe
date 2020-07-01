from pymongo import MongoClient

from ..env import TEST_DATABASE

test = MongoClient(TEST_DATABASE).get_default_database()

if __name__ == "__main__":
    
    for x in test.mqttpy.find():
        print(x)
