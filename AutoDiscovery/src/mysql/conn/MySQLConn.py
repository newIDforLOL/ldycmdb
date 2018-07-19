# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.IniUtils import IniUtils


class MySQLConn:

    def __init__(self):
        self.getIni()

    def getIni(self):
        self.ini = IniUtils("mysql.ini")

    def getConnStr(self):
        host = self.ini.getProperties("mysql", "host")
        port = self.ini.getProperties("mysql", "port")
        username = self.ini.getProperties("mysql", "username")
        password = self.ini.getProperties("mysql", "password")
        database = self.ini.getProperties("mysql", "database")
        return str(r"mysql+mysqldb://%s:" + '%s' + "@%s:%s/%s?charset=utf8") % (
            username, password, host, port, database
        )

    def getEngine(self):
        connStr = self.getConnStr()
        poolSize = self.ini.getProperties("mysql", "poolSize")
        maxOverflow = self.ini.getProperties("mysql", "maxOverflow")
        poolRecycle = self.ini.getProperties("mysql", "poolRecycle")
        poolTimeout = self.ini.getProperties("mysql", "poolTimeout")
        engine = create_engine(
            connStr, pool_size=poolSize, max_overflow=maxOverflow, pool_recycle=poolRecycle, pool_timeout=poolTimeout
        )
        return engine

    def getConn(self):
        return self.getEngine().raw_connection()

    def getSession(self):
        dbSession = sessionmaker(self.getEngine())
        return dbSession()

    def execQuery(self, query):
        conn = self.getConn()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return cursor.fetchall()
