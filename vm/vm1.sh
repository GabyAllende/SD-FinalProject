
#!/bin/bash

# Docker network
docker network create mis-libros-net

#Broker
docker run -it --rm -p 1883:1883 -d --network mis-libros-net --name broker -v $PWD/broker/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto

# Nodejs publishers

cd publisher/
docker build . -t image-publisher:1.0.0

declare -a names=(pub_1 pub_2 pub_3 pub_4 pub_5)

for (( j=0; j<5; j++ ));
do
  docker run -e PORT=1883 --rm -d -e TOPIC=control -e HOST=broker --network mis-libros-net --name "${names[$j]}" image-publisher:1.0.0
done