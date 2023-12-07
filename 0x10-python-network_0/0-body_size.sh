#!/bin/bash
# send a request to an URL with curl, and displays size of the body of the response
curl -s "$1" | wc -c
