# coding: utf-8


from utils.IniUtils import IniUtils
import subprocess
import re
import json


class NmapService(object):

    def scan(self):
        nmapCmd = self.getCmd()
        print(nmapCmd)
        p = subprocess.Popen(nmapCmd, stdout=subprocess.PIPE,  shell=True)
        self.parseNmapResult(p.stdout.read())

    def getCmd(self):
        ini = IniUtils("nmap.ini")
        nmapBin = ini.getProperties("nmap", "bin")
        param = ini.getProperties("nmap", "param")
        networkSegment = ini.getProperties("nmap", "networkSegment")
        return "%s %s %s" % (nmapBin, param, networkSegment)
    
    def parseNmapResult(self, nmapResult):
        nr_arr = nmapResult.split('\n')
        ipreg = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        osreg = re.compile(r'OS.*:(.+?), ')

        ret = []
        ip = ""
        os = ""
        for line in nr_arr:
            if line == "" and ip:
                s = {"ip":''.join(ip).strip() ,"os": ''.join(os).strip()}
                ret.append(s)
                ip = ""
                os = ""
            else:
                tip = re.findall(ipreg,line)
                if tip:
                    ip = tip
                tos = re.findall(osreg,line)
                if tos:
                    os = tos
        print json.dumps(ret)
