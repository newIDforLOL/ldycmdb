# coding: utf-8


from utils.IniUtils import IniUtils
import subprocess


class NmapService(object):

    def scan(self):
        nmapCmd = self.getCmd()
        print(nmapCmd)
        # p = subprocess.Popen(nmapCmd, stdout=subprocess.PIPE)
        # self.parseNmapResult(p.stdout.read())

    def getCmd(self):
        ini = IniUtils("nmap.ini")
        nmapBin = ini.getProperties("nmap", "bin")
        param = ini.getProperties("nmap", "param")
        ifDevice = ini.getProperties("nmap", "ifDevice")
        portRange = ini.getProperties("nmap", "portRange")
        networkSegment = ini.getProperties("nmap", "networkSegment")
        return "%s %s -e %s -p%s %s" % (nmapBin, param, ifDevice, portRange, networkSegment)
    
    def parseNmapResult(self, nmapResult):
        print(nmapResult)
