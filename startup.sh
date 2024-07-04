docker container create -it --name C1 ubuntu:16.10
docker start C1
docker exec -it C1 bash -c "apt update && apt upgrade -y && apt install openssh-client && apt autoremove -y && apt clean && exit"
docker container create -it --name C2 ubuntu:18.10
docker start C2
docker exec -it C2 bash -c "apt update && apt upgrade -y && apt install openssh-client && apt autoremove -y && apt clean && exit"
docker container create -it --name C3 ubuntu:20.10
docker start C3
docker exec -it C3 bash -c "apt update && apt upgrade -y && apt install openssh-client && apt autoremove -y && apt clean && exit"
docker container create -it --name C4S1 ubuntu:22.10
docker start C4S1
docker exec -it C4S1 bash -c "apt update && apt upgrade -y && apt install openssh-client openssh-server && apt autoremove -y && apt clean && exit"

