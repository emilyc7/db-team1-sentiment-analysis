#!/bin/sh
docker stop $(docker ps -a -q) ; docker build -t test1 . ; docker run -p 4000:5000 test1
