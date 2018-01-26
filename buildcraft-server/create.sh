#!/bin/bash

buildcraft_url="http://www.mod-buildcraft.com/releases/BuildCraft/7.1.21/buildcraft-7.1.21.jar"
buildcraft_filename="buildcraft-7.1.21.jar"

mkdir -p "/srv/docker/buildcraft-server/mods"

echo "Downloading BuildCraft..."
wget -q "$buildcraft_url" -O "/srv/docker/buildcraft-server/mods/$buildcraft_filename"

echo "Initializing container '$container_name'..."
docker-compose up

echo "Done!"
