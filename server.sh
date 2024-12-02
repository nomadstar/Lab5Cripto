apt-get install -y openssh-server
USER=prueba
PASS='prueba'
useradd -m -s /bin/bash $USER && echo "$USER:$PASS" | chpasswd

if [ "$1" = true ]; then
    apt-get install -y wget g++ make zlib1g-dev libssl-dev build-essential libpam0g-dev libselinux1-dev libaudit-dev tcpdump
    wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.0p1.tar.gz
    tar -xzf openssh-9.0p1.tar.gz
    cd openssh-9.0p1
    sed -i 's/^#define SSH_VERSION.*/#define SSH_VERSION "OpenSSH_?"/' version.h
    sleep 5
    ./configure
    sleep 5
    make
    sleep 5
    make install
fi


tail -f /dev/null
