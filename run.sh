#!/bin/bash

FILE=./config/.env

if test -f "$FILE"; then
  # set .env vars
  export $(echo $(cat $FILE | sed 's/#.*//g'| xargs) | envsubst)
else
  echo "Config file \"$FILE\" not found."
fi

# run bot
python3 src/main.py

