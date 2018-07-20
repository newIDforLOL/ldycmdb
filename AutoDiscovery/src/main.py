# coding: utf-8


from service.NmapService import NmapService
from service.test.TestService import TestService


def main():
    nmapService = NmapService()
    nmapService.scan()
    testService = TestService()
    testService.testSet()
    testService.testGet()


if __name__ == "__main__":
    main()
