#!/usr/bin/python3
"""
Module displays displays
email decoded in utf-8.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    address = {'email': sys.argv[2]}

    res = urllib.parse.urlencode(address)
    res = res.encode('ascii')
    req = urllib.request.Request(url, res)

    with urllib.request.urlopen(req) as response:
        output = response.read()
        print(output.decode('utf-8'))
