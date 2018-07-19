# coding: utf-8


import os
from configparser import ConfigParser


class IniUtils(object):

    def __init__(self, iniFileName):
        currentPath = os.path.abspath(__file__)
        configFilePath = os.path.abspath(os.path.dirname(currentPath) + os.path.sep + "../../resources/ini")
        configFile = os.path.join(configFilePath, iniFileName)
        self.cfg = ConfigParser()
        self.cfg.read(configFile)

    def getSections(self):
        return self.cfg.sections()

    def getProperties(self, sectionName, keyName):
        return self.cfg.get(sectionName, keyName)
