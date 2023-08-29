from fastapi import FastAPI
import users,driver,greet

app = FastAPI()

@app.get('/')
def root():
    return('Root Page')

app.include_router(users.router)
app.include_router(driver.router)
app.include_router(greet.router)