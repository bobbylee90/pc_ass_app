from fastapi import APIRouter
from utils.api_model import AccountInfo

router = APIRouter()

@router.get("/dbcheck")
async def db_checker():
    return {"status": "db is alive"}