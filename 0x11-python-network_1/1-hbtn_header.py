#!/usr/bin/python3
"""
Module displays value of
X-Request-Id variable found
in header of response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        output = (dict(response.headers).get("X-Request-Id"))
        print(output)
