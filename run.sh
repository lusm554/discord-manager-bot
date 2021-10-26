#!/bin/bash

container_name="minecraft_discord_bot"

docker build -t $container_name .

docker run --name $container_name -d $container_name 
