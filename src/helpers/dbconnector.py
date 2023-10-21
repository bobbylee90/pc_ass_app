from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.helpers.db_models import DbBase

class MysqlConnector():

    def __init__(self) -> None:
        self.username = "mainhost"
        self.password = "test123"
        self.db_host = "mysql"
        self.db_port = 3306
        self.db_name = "default"
        self.template_engine = "mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.engine = self.get_engine()
        self.sess = self.create_session()

    def get_engine(self):
        eg_conf = self.template_engine.format(db_username=self.username,
            db_password=self.password,
            db_host=self.db_host,
            db_port=self.db_port,
            db_name =self.db_name)
        return create_engine(eg_conf, echo=True)
    
    def create_session(self):
        return Session(bind=self.engine)
    
    def create_tables(self)-> bool:
        status: bool  = False
        try:
            DbBase.metadata.create_all(bind=self.engine)
            status = True
        except Exception as e:
            status = False
            print(f"create tables fails....")
        return status



    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.sess.close_all()
        self.engine.dispose()