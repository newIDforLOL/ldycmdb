# coding: utf-8


from utils.IniUtils import IniUtils


class NmapService(object):

    def scan(self):
        nmapCmd = self.getCmd()
        print(nmapCmd)

    def getCmd(self):
        ini = IniUtils("nmap.ini")
        param = ini.getProperties("nmap", "param")
        ifDevice = ini.getProperties("nmap", "ifDevice")
        portRange = ini.getProperties("nmap", "portRange")
        networkSegment = ini.getProperties("nmap", "networkSegment")
        return "nmap %s -e%s -p%s %s" % (param, ifDevice, portRange, networkSegment)
