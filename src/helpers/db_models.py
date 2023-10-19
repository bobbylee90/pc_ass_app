from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import ForeignKey, Text, create_engine, String, select

class DbBase(DeclarativeBase):
    pass

class Accounts(DbBase):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255),nullable=False)
    password: Mapped[str] = mapped_column(String(255),nullable=False)
    info: Mapped["Info"] = relationship(back_populates="account")

    def __repr__(self) -> str:
        ret: str = ""
        for key, val in self.__dict__.items():
            ret += f"{key}:{val}\n"
        return ret
    

    

class Info(DbBase):
    __tablename__ = "info"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    fullname: Mapped[str] = mapped_column(String(255),nullable=True)
    email: Mapped[str] = mapped_column(String(255),nullable=False)
    phone: Mapped[str] = mapped_column(String(255),nullable=True)
    biography: Mapped[str] = mapped_column(Text, nullable=True)
    account: Mapped["Accounts"] = relationship(back_populates="info")

    def __repr__(self) -> str:
        ret: str = ""
        for key, val in self.__dict__.items():
            ret += f"{key}:{val}\n"
        return ret
    
    def __str__(self) -> str:
        return f"by user : {self.account.username}\n{self.biography}"
    
if __name__ == "__main__":
    db_username = "mainhost"
    db_password = "test123"
    db_host = "mysql"
    db_port = 3306
    db_name = "default"
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
    DbBase.metadata.create_all(bind=engine)

    # acc1 = Accounts(username="testing123", password="pass123", info=Info(
    #     fullname="Mike Steward",
    #     email="mikesteward@gmail.com",
    #     phone="+886999880056",
    #     biography="workaholics, love to code. No personal like. Boring"
    # ))

    # acc2 = Accounts(username="testing456", password="pass456", info=Info(
    #     fullname="Jenny Lin",
    #     email="jlin@gmail.com",
    #     phone="+886888990053",
    #     biography="most pretty girl in the world!!!"
    # ))

    # with Session(bind=engine) as sess:
    #     sess.add_all([acc1, acc2])
    #     sess.commit()

    statement1 = select(Accounts).where(Accounts.username.in_(["testing123", "testing456"]))
    with Session(bind=engine) as sess2:
        result = sess2.scalars(statement=statement1)
        for acc in result:
            print(acc)
        print()
        info = sess2.query(Info).all()
        for inf in info:
            print(inf)