from motor.motor_asyncio import AsyncIOMotorClient

# uri is used to connect our db to python 

uri = 'mongodb://localhost:27017'
client = AsyncIOMotorClient(uri)

database = client.auth_db

user_collection = database.user_coll

def get_db():
    return database