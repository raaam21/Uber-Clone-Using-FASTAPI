from motor.motor_asyncio import AsyncIOMotorClient

# uri is used to connect our db to python 

# for desktop mongodb
uri = 'mongodb://localhost:27017'

# for cloud based mongodb
# uri = 'mongodb+srv://yoursram18:Optiplex45@cluster0.ohh3mb0.mongodb.net/?retryWrites=true&w=majority'

client = AsyncIOMotorClient(uri)

database = client.auth_db

user_collection = database.user_coll

def get_db():
    return database