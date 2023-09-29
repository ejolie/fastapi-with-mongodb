import os

import motor.motor_asyncio

DATABASE_URL = os.environ["MONGODB_URL"]

# Create a new client and connect to the server
# client = MongoClient(uri)
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

db = client.college_db

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
