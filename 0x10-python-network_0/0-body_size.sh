#!/bin/bash
# displays size of body of response
curl -sI "$1" | wc -c
