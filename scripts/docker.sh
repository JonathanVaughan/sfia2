#!/bin/bash
source ~/.bashrc
docker-compose build
docker push jonvaughan2000/service1:latest
docker push jonvaughan2000/service2:latest
docker push jonvaughan2000/service3:latest
docker push jonvaughan2000/service4:latest
docker stack deploy --compose-file docker-compose.yaml stack1
docker stack deploy --compose-file docker-compose.yaml holidaystack