docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker network rm mis-libros-net
docker rmi image-publisher:1.0.0

