from fastapi import APIRouter
import sqlalchemy as sa
from sqlalchemy.orm import Session
from src.helpers.db_models import Accounts, Infos
from src.helpers.api_models import Account, Info
from src.helpers.dbconnector import MysqlConnector

router = APIRouter()

@router.get("/dbcheck/")
async def db_checker():
    db_name: list = []
    ret: dict = {}
    with MysqlConnector() as conn:
        insp = sa.inspect(conn.engine)
        db_name = insp.get_schema_names()
    i = 1
    for db in db_name:
        ret[f"db-{i}"] = db
        i += 1
    return {"available-db": ret}

@router.get("/bydbname/{dbname}")
async def is_db_exits(dbname: str):
    db_name: list = []
    with MysqlConnector() as conn:
        insp = sa.inspect(conn.engine)
        db_name = insp.get_schema_names()

    return {dbname: True if dbname in db_name else False}

@router.post("/username/info", response_model=Account)
async def get_acc_by_username(username: str):
    temp: Accounts =  None
    with MysqlConnector() as conn:
        temp = conn.sess.query(Accounts).where(Accounts.username == username).first()
        print(temp)
    return temp.return_api_models() if temp else Account(username="",password="", info=Info(fullname="",email="",phone="",biography=""))

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
        conn.sess.add(account)
        conn.sess.commit()
        temp = []
        result = conn.sess.query(Accounts, Infos).filter(Accounts.id == Infos.account_id).all()
        # result = sess.query(Accounts, Infos).filter(Accounts.id == Infos.account_id).filter(Infos.phone.like("+886%")).all()
        for res in result:
            temp.append({**res[0].customdict(), **res[1].customdict()})
        ret["dbrecords"] = temp
    return ret

@router.put("/update/info")
async def update_by_username(acc: Account):
    ret: dict = {"updated" : "false"}
    temp: list = []
    with MysqlConnector() as conn:
        target_record = conn.sess.query(Accounts).filter(Accounts.username == acc.username).first()
        if target_record:
            target_record.update_from_account(acc=acc)
            conn.sess.commit()
            ret["updated"] = "true"
        result = conn.sess.query(Accounts, Infos).filter(Accounts.id == Infos.account_id).all()
        for res in result:
            temp.append({**res[0].customdict(), **res[1].customdict()})
    ret["records"] = temp
    return ret

@router.delete("/delete/user")
async def create_new_account(username: str):
    ret: dict = {"deleted" : "false"}
    temp: list = []
    with MysqlConnector() as conn:
        target_record = conn.sess.query(Accounts).filter(Accounts.username == username).first()
        if target_record:
            conn.sess.delete(target_record)
            conn.sess.commit()
            ret["deleted"] = "true"
        result = conn.sess.query(Accounts, Infos).filter(Accounts.id == Infos.account_id).all()
        for res in result:
            temp.append({**res[0].customdict(), **res[1].customdict()})
    ret["records"] = temp
    return ret
        


        

