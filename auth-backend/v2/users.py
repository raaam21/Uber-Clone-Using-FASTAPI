from fastapi import APIRouter,Response
import models 
import utils
from datetime import datetime
import database_manager
import random
from typing import List


router = APIRouter()


@router.post('/api/v2/signup',response_model = models.UserCreateResponse)
async def signup(user_obj:models.UserCreateRequest):
    db = database_manager.get_db()
    user_coll = db.user_coll
    
    user_obj=user_obj.dict()
    
    result =await user_coll.find_one({"email" : user_obj['email']})
    
    if result:
        return {"Status":"Failure","message":"User Already exist !!"}
    
    user_dict={}
    user_dict['id'] = random.randint(1,9999999)
    user_dict['name'] = user_obj['name']
    user_dict['email'] = user_obj['email']
    # hashing 
    user_dict['password'] = utils.hash(user_obj['password'])
    user_dict['created_at']= datetime.utcnow()
    
    
    user_coll.insert_one(user_dict)
        
    return user_dict


@router.post('/api/v2/signin')
async def signin(user_req:dict,response:Response):
    
    db = database_manager.get_db()
    user_coll = db.user_coll
    
    user_doc = await user_coll.find_one({"email":user_req["email"]})
    
    if user_doc:
        if utils.hash(user_req['password']) == user_doc['password']:
            # set cookies
            
            response.set_cookie("access_token"),
            
            return {"status":"success","message":"OK","access_token":user_doc['id'],"expiry":0} 
        
    
    return {"Status":"Failure","message":"NOT OK!!"}




@router.get('/api/v2/users',response_model = List[models.UserCreateResponse])
async def get_all_users():
    
    db = database_manager.get_db()
    user_coll = db.user_coll
    
    docs = user_coll.find()
    response = []
    async for doc in docs:
        response.append(models.UserCreateResponse(**doc))
    return response



@router.post('/api/v2/signout')
async def signout(response:Response):
    response.delete_cookie("access_token")      
    return {"status":"success","message":"Logout DOne"} 
    