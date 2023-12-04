#!/bin/bash
# displays the size of the body from the requested URL
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
