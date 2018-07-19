# coding: utf-8


from service.NmapService import NmapService


class DiscoveryService(object):

    def __init__(self):
        pass

    def discovery(self):
        nmapService = NmapService()
        nmapService.scan()
