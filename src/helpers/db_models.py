from copy import deepcopy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import ForeignKey, Text, create_engine, String, select
from src.helpers.api_models import Account, Info

class DbBase(DeclarativeBase):
    pass

class Accounts(DbBase):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255),nullable=False)
    password: Mapped[str] = mapped_column(String(255),nullable=False)
    info: Mapped["Infos"] = relationship(back_populates="account")

    def __init__(self, username: str, password: str, info: "Infos"):
        self.username = username
        self.password = password
        self.info = info
    
    def customdict(self)-> dict: 
        temp: dict = deepcopy(self.__dict__)
        temp.pop("_sa_instance_state")
        temp = {**temp, **self.info.customdict()}
        return temp 

    def return_api_models(self) -> Account :
        return Account(username=self.username, password=self.password, info=Info(
            fullname=self.info.fullname,
            email=self.info.email,
            phone=self.info.phone,
            biography=self.info.biography
        ))

    

class Infos(DbBase):
    __tablename__ = "infos"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    fullname: Mapped[str] = mapped_column(String(255),nullable=True)
    email: Mapped[str] = mapped_column(String(255),nullable=False)
    phone: Mapped[str] = mapped_column(String(255),nullable=True)
    biography: Mapped[str] = mapped_column(Text, nullable=True)
    account: Mapped["Accounts"] = relationship(back_populates="info")

    def __init__(self, fullname: str, email: str, phone: str, biography: str):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.biography = biography
    
    def customdict(self)-> dict: 
        temp: dict = deepcopy(self.__dict__)
        temp.pop("_sa_instance_state")
        return temp   
    
    def return_api_models(self) -> Info :
        return Info(fullname=self.fullname, email=self.email, phone=self.phone, biography=self.biography)
    
if __name__ == "__main__":
    db_username = "mainhost"
    db_password = "test123"
    db_host = "mysql"
    db_port = 3306
    db_name = "default"
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
    DbBase.metadata.create_all(bind=engine)

    acc1 = Accounts(username="testing123", password="pass123", info=Infos(
        fullname="Mike Steward",
        email="mikesteward@gmail.com",
        phone="+886999880056",
        biography="workaholics, love to code. No personal like. Boring"
    ))

    acc2 = Accounts(username="testing456", password="pass456", info=Infos(
        fullname="Jenny Lin",
        email="jlin@gmail.com",
        phone="+886888990053",
        biography="most pretty girl in the world!!!"
    ))

    acc3 = Accounts(username="testing789", password="pass789", info=Infos(
        fullname="Jonny",
        email="john-ny@gmail.com",
        phone="+886900880056",
        biography="John is preferable, Thanks."
    ))

    acc4 = Accounts(username="testing101112", password="pass101112", info=Infos(
        fullname="Bing Chat",
        email="bchat@gmail.com",
        phone="+886777990059",
        biography="Do you know I am a LLM?"
    ))

    with Session(bind=engine) as sess:
        sess.add_all([acc1, acc2, acc3, acc4])
        sess.commit()

    # statement1 = select(Accounts).where(Accounts.username.in_(["testing123", "testing456"]))
    # with Session(bind=engine) as sess2:
    #     # result = sess2.scalars(statement=statement1)
    #     # for acc in result:
    #     #     print(acc)
    #     # print()
    #     # info = sess2.query(Info).all()
    #     # for inf in info:
    #     #     print(inf)

    #     results = sess2.query(Accounts, Infos).filter(Accounts.id == Infos.account_id).filter(Infos.phone.like("+886%")).all()
    #     print(results)
    #     print(type(results))
