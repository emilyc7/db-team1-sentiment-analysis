#!/usr/bin/env bash
docker stop $(docker ps -a -q) ;
docker rm $(docker ps -aq) ;
docker rmi $(docker images -q) ;
docker build -t test1 . ;
docker run -p 4000:5000 test1
