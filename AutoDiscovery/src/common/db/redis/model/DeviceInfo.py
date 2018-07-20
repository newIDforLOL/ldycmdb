# coding: utf-8


class DeviceInfo(object):

    __slots__ = (
        "deviceId",
        "code",
        "ip",
        "name",
        "hostName",
        "os",
        "comment",
    )

    def __init__(self, deviceId=None, code=None, ip=None, name=None, hostName=None, os=None, comment=None):
        self.deviceId = deviceId
        self.code = code
        self.ip = ip
        self.name = name
        self.hostName = hostName
        self.os = os
        self.comment = comment

    def toDict(self):
        return {
            "deviceId": self.deviceId,
            "code": self.code,
            "ip": self.ip,
            "name": self.name,
            "hostName": self.hostName,
            "os": self.os,
            "comment": self.comment,
        }
