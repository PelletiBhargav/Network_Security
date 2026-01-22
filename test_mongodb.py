import os
import pymongo
import certifi
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000
)

client.admin.command("ping")
print("MongoDB Atlas connected successfully!")
