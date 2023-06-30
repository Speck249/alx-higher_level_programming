#!/usr/bin/python3
"""
Module displays value of
X-Request-Id variable found
in header of response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    output = res.headers.get("X-Request-Id")
    print(output)
