#!/bin/bash
# Send a DELETE request to a given URL and display the body of the response
curl -s "$1" -X DELETE
