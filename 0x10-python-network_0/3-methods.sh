#!/bin/bash
# displays all HTTP methods server will accept.
curl -sI -X OPTIONS "$1" | grep -i "Allow" | tr -d '\r' | sed 's/Allow: //I'
