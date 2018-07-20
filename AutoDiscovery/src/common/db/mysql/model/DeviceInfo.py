# coding: utf-8


from sqlalchemy import Column
from sqlalchemy.types import String
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class DeviceInfo(BaseModel):
    __tablename__ = 'device_info'

    id = Column(String, primary_key=True)
    ip = Column(String, index=True)
    device_name = Column(String, index=True)
    host_name = Column(String, index=True)
    os = Column(String, index=True)
    comment = Column(String, index=True)
