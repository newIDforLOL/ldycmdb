# coding: utf-8


from common.db.redis.conn.RedisConn import RedisConn


class TestService(object):

    def __init__(self):
        self.r = self.getRedis()

    def getRedis(self):
        redisConn = RedisConn()
        return redisConn.getStrictRedis()

    def testSet(self):
        self.r.set("testKey", "testValue")

    def testGet(self):
        print(self.r.get("testKey"))
