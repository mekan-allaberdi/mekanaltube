from pymongo import MongoClient

DB_NAME = 'mytubedb'
DB_URI = 'mongodb+srv://mekan:ezizhan>@cluster0.nsaos.mongodb.net/mytubedb?retryWrites=true&w=majority'
client = MongoClient(DB_URI)
db = client[DB_NAME]
