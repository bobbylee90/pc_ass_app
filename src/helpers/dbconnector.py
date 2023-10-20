from sqlalchemy import create_engine

class MysqlConnector():

    def __init__(self) -> None:
        self.username = "mainhost"
        self.password = "test123"
        self.db_host = "mysql"
        self.db_port = 3306
        self.db_name = "default"
        self.template_engine = "mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.engine = self.get_engine()

    def get_engine(self):
        eg_conf = self.template_engine.format(db_username=self.username,
            db_password=self.password,
            db_host=self.db_host,
            db_port=self.db_port,
            db_name =self.db_name)
        return create_engine(eg_conf, echo=True)


    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass