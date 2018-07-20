# coding: utf-8


from utils.IniUtils import IniUtils
import redis


class RedisConn(object):

    def __init__(self):
        self.getIni()

    def getIni(self):
        self.ini = IniUtils("redis.ini")

    def getStrictRedis(self):
        pool = redis.ConnectionPool(
            host=self.ini.getProperties("redis", "host"),
            port=self.ini.getProperties("redis", "port"),
            password=self.ini.getProperties("redis", "auth"),
            db=self.ini.getProperties("redis", "db"),
            max_connections=int(self.ini.getProperties("redis", "maxConnections"))
        )
        return redis.StrictRedis(charset='utf-8', connection_pool=pool, decode_responses=True)
