from fastapi import FastAPI
from datetime import datetime
import random
from v2 import utils


app=FastAPI()

user_coll=[{
    "id" : 1,
    "name" : "Ram",
    "email" : "ram@gmail.com",
    "password" : "OPtiplex45@",
    # Creating time stamp
    "created_at" : '31-07-23 18:19:00'
    },{
    "id" : 2,
    "name" : "Raj",
    "email" : "raj@gmail.com",
    "password" : "plex45@",
    # Creating time stamp
    "created_at" : '31-07-23 18:20:00'
    
}]


@app.get('/')
def hello():
    return('Landing Page using FastAPI')


@app.post('/api/v1/signup')
def signup(user_obj:dict):
    
    for user in user_coll:
        if user_obj["email"]==user["email"]:
            return {"Status":"Failure","message":"User Already exist !!"}
    
    user_dict={}
    user_dict["id"] = random.randint(1,9999999)
    user_dict["name"] = user_obj["name"]
    user_dict["email"] = user_obj["email"]
    # hashing 
    user_dict["password"] = utils.hash(user_obj["password"])
    user_dict['created_at']=datetime.utcnow()
    
    
    user_coll.append(user_dict)
        
    return user_dict

@app.post('/api/v1/signin')
def signin(user_req:dict):
    
    for user in user_coll:
        if user_req["email"]==user["email"]:
            if user_req["password"]==user["password"]:
                # token session and it's expiry
                return {"Status":"Success","message":"OK!!","access_token":user["id"],"expiry":60}
    
    return {"Status":"Failure","message":"NOT OK!!"}

@app.get('/api/v1/getusers')
def get_users():
    return user_coll


# @app.post('/api/v1/search/drivers')
# def signin(user_req:dict):
    
#     for user in user_coll:
#         if user_req["email"]==user["email"]:
#             if user_req["password"]==user["password"]:
#                 # token session and it's expiry
#                 return {"Status":"Success","message":"OK!!","access_token":user["id"],"expiry":60}
    
#     return {"Status":"Failure","message":"NOT OK!!"}