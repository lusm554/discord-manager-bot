#!/bin/bash

docker image rm -f minecraft_discord_bot 
docker image prune -f 
docker container rm -f minecraft_discord_bot
