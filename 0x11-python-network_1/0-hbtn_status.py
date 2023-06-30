#!/usr/bin/python3
"""
Module fetch internet resources
using urllib package.
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        output = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(output)))
        print('\t- content: {}'.format(output))
        print('\t- utf8 content: {}'.format(output.decode('utf-8')))
