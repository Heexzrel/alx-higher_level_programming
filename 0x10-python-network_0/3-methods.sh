#!/bin/bash
# Display all the  HTTP methods the server of a given URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
