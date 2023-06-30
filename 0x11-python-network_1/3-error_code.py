#!/usr/bin/python3
"""
Module urllib.error.HTTPError
exceptions.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            output = response.read().decode('utf-8')
            print(output)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
