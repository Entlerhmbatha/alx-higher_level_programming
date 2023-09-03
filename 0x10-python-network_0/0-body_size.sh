#!/bin/bash
#Send a request to URL && display size of body
curl -s "$1" | wc -c
