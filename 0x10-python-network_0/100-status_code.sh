#!/bin/bash
#get statue code from the given URL
curl -so /dev/null --write-out "%{http_code}" "$1"
