# coding: utf-8


from common.db.redis.conn.RedisConn import RedisConn
from common.db.redis.model.DeviceInfo import DeviceInfo


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

    def test(self):
        print(123123)
        device = DeviceInfo()
        device.deviceId = 1
        device.code = "kjIHknfdkaski"
        device.ip = "127.0.0.1"
        print(device.toDict())


if __name__ == "__main__":
    t = TestService()
    t.test()