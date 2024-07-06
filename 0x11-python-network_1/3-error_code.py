#!/usr/bin/python3
"""A script that takes in a URL
sends a request to the URL and
displays the body of the response"""
from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as respo:
            print(respo.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.status))
