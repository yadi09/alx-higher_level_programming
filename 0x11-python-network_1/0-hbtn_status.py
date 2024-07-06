#!/usr/bin/python3
"A script that fetches https://alx-intranet.hbtn.io/status"
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode()))
