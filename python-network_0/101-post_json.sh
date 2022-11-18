#!/bin/bash
# comment
curl -sX POST -H "Content-Type: application/json" -d @"$2"  "$1"
