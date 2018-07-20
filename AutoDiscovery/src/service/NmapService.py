# coding: utf-8


from utils.IniUtils import IniUtils
import subprocess
import sys
import re
import json


class NmapService(object):

    def scan(self):
        nmapCmd = self.getCmd()
        print(nmapCmd)
        p = subprocess.Popen(nmapCmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.parseNmapResult(p)

    def getCmd(self):
        ini = IniUtils("nmap.ini")
        nmapBin = ini.getProperties("nmap", "bin")
        param = ini.getProperties("nmap", "param")
        networkSegment = ini.getProperties("nmap", "networkSegment")
        return "\"%s\" %s %s" % (nmapBin, param, networkSegment)

    def getStdout(self, popenResult):
        out = popenResult.stdout.read()
        err = popenResult.stderr.read()
        if err:
            if sys.platform == "win32":
                raise Exception(err.decode("gbk"))
            else:
                raise Exception(err.decode("utf-8"))
        if sys.platform == "win32":
            return out.decode("gbk")
        else:
            return out.decode("utf-8")

    def parseNmapResult(self, nmapResult):
        nmapResult = self.getStdout(nmapResult)
        print(type(nmapResult))
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
        print(json.dumps(ret))
