# coding: utf-8


from utils.IniUtils import IniUtils
import subprocess


class NmapService(object):

    def scan(self):
        nmapCmd = self.getCmd()
        print(nmapCmd)
        p = subprocess.Popen(nmapCmd, stdout=subprocess.PIPE)
        parseNmapResult(p.stdout.read())

    def getCmd(self):
        ini = IniUtils("nmap.ini")
        nmapbin = ini.getProperties("nmap", "bin")
        param = ini.getProperties("nmap", "param")
        ifDevice = ini.getProperties("nmap", "ifDevice")
        portRange = ini.getProperties("nmap", "portRange")
        networkSegment = ini.getProperties("nmap", "networkSegment")
        return "%s %s -e %s -p%s %s" % (nmapbin, param, ifDevice, portRange, networkSegment)
    
    def parseNmapResult(nmapResult):
        print(nmapResult)
