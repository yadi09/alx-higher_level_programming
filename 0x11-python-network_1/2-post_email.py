#!/usr/bin/python3
"""script that takes in a URL and an email
sends a POST request to the passed URL
with the email as a parameter"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    query_str = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    url = sys.argv[1]
    requ = request.Request(url, query_str)
    with request.urlopen(requ) as respo:
        data = respo.read().decode('utf-8')
        print(data)
