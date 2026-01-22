from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://pelletivenkatabhargav03_db_user1:Admin%40123@cluster0.hb3aqf8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
