from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import users,driver,greet

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return 'this is using fast api'

app.include_router(users.router)
app.include_router(driver.router)
app.include_router(greet.router)