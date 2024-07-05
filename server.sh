apt-get install -y openssh-server
USER=prueba
PASS='prueba'
useradd -m -s /bin/bash $USER && echo "$USER:$PASS" | chpasswd
tail -f /dev/null
# escribe service ssh start para partir (el archivo no lo hace porque, para que tan flojo?)