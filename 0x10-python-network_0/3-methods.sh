#!/bin/bash
# allow methods on the server
curl -sI $1 | grep Allow | cut -d' ' -f2
