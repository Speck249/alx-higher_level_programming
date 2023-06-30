#!/usr/bin/python3
"""
Module displays displays
email decoded in utf-8.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    address = {'email': sys.argv[2]}
    output = requests.post(url, address)

    print(output.text)
