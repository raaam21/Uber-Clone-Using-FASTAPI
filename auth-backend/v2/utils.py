# from passlib.context import CryptContext

import hashlib

from typing import *

# pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash(plain_text:str)-> str: 
    return hashlib.md5(plain_text.encode('utf-8'),usedforsecurity=True).hexdigest()