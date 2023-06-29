#!/bin/bash
# displays size of body of response
curl -sSL "$1" | wc -c
