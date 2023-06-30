#!/usr/bin/python3
"""
Module sends POST request to
http://0.0.0.0:5000/search_user.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    elif len(sys.argv) == 1:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    param = {'q': q}
    res = requests.post(url, param)

    try:
        output = res.json()
        if output:
            print("[{}] {}".format(output["id"], output["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
