from pymongo import MongoClient

DB_NAME = "mytubedb"
client = MongoClient('mongodb://localhost:27017/')
db = client[DB_NAME]
