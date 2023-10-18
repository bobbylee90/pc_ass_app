from sqlalchemy import create_engine


class MysqlConnector():

    def __init__(self) -> None:
        self.username = "mainhost"
        self.password = "test123"
        self.db_host = "mysql"
        self.db_port = 3306
        self.db_name = "default"

    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass