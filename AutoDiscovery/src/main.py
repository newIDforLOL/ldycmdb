# coding: utf-8


from service.NmapService import NmapService


def main():
    nmapService = NmapService()
    nmapService.scan()


if __name__ == "__main__":
    main()
