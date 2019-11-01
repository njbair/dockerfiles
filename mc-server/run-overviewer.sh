#!/bin/bash

docker pull mide/minecraft-overviewer:latest

docker run \
	--rm \
        -e MINECRAFT_VERSION="1.14.4" \
	-v `pwd`/overviewer/config.py:/home/minecraft/config.py \
        -v /srv/docker/minecraft-server:/home/minecraft/server/:ro \
        -v /srv/docker/minecraft-overviewer:/home/minecraft/render/:rw \
        mide/minecraft-overviewer:latest

#rsync -az /srv/docker/minecraft-overviewer/* njbai.rs:/var/www/nickbair.net/minecraft-overviewer/
