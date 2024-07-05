ARG version
ARG connumber
FROM ubuntu:$version
RUN sed -i -E 's#http://[^/]+\.ubuntu\.com/ubuntu#http://old-releases.ubuntu.com/ubuntu#g' /etc/apt/sources.list
RUN perl -pi -e 's/^Prompt=.*/Prompt=normal/' /etc/update-manager/release-upgrades
RUN apt-get update && apt-get upgrade -y
RUN if [ $connumber == "4" ]; then apt-get install -y openssh-client openssh-server; else apt-get install -y openssh-client; fi
ENV USER=test${connumber}
ENV PASS='test${connumber}'
RUN useradd -m -s /bin/bash $USER && echo "$USER:$PASS" | chpasswd