#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    respo = requests.get("https://alx-intranet.hbtn.io/status")
    data = respo.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
