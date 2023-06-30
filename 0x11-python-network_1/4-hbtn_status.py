#!/usr/bin/python3
"""
Module fetches url
using requests.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    output = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(output.text)))
    print("\t- content: {}".format(output.text))
