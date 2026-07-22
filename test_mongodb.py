from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://atultewari26always_db_user:<@password>.varai4s.mongodb.net/?appName=Db2"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    