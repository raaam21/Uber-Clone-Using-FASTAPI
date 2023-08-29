from fastapi import FastAPI,APIRouter

router = APIRouter()

@router.post('/api/v2/search/nearby_drivers')
def nearby_drivers(access_token:str):
    pass