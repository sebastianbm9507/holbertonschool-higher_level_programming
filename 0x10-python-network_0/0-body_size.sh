#!/bin/bash
# Extract the content length of a header response
curl -sI  "$1" | grep Content-Length | cut -d'' -f2 
