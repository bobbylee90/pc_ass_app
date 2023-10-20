from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.helpers.db_models import Accounts, Infos
from src.helpers.api_models import Account
from src.helpers.dbconnector import MysqlConnector

router = APIRouter()

@router.get("/dbcheck/{dbname}")
async def db_checker(dbname: str):
    return {"status": "db is alive"}

@router.post("/checkacc/")
async def get_acc_by_username(username: str):
    print(f"username : {username}, type = {type(username)}")
    return username

@router.post("/addnew/")
async def create_new_account(acc: Account):
    ret:dict = {"dbrecords": ""} 
    account: Accounts = Accounts(username=acc.username, password=acc.password, info=Infos(
        fullname=acc.info.fullname,
        email=acc.info.email,
        phone=acc.info.phone,
        biography=acc.info.biography
    ))
    with MysqlConnector() as conn:
        sess =  Session(bind=conn.engine)
        sess.add(account)
        sess.commit()
        temp = []
        result = sess.query(Accounts, Infos).filter(Accounts.id == Infos.account_id).filter(Infos.phone.like("+886%")).all()
        for res in result:
            temp.append({**res[0].customdict(), **res[1].customdict()})
        ret["dbrecords"] = temp
    return ret

