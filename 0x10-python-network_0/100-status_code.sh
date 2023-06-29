#!/bin/bash
# displays only the status code of response
curl -s -o /dev/null -w "%{http_code}\n" "$1"
