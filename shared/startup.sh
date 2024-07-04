apt update
apt upgrade -y
apt install openssh-client

if [ -z "$1" ]; then
    echo "Not special parameter"
elif [ "$1" = "Super" ]; then
    echo "Making super container"
    apt install openssh-server
fi