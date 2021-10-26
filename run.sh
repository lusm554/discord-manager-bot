#!/bin/bash

# set .env vars
export $(echo $(cat ./config/.env | sed 's/#.*//g'| xargs) | envsubst)

# run bot
python3 src/main.py

