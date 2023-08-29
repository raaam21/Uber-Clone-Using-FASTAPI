from fastapi import APIRouter

router = APIRouter()


@router.get('/greet')
def hello():
    return('Landing Page using FastAPI')