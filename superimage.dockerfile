ARG version
ARG server
FROM ubuntu:$version
RUN sed -i -E 's#http://[^/]+\.ubuntu\.com/ubuntu#http://old-releases.ubuntu.com/ubuntu#g' /etc/apt/sources.list
RUN perl -pi -e 's/^Prompt=.*/Prompt=normal/' /etc/update-manager/release-upgrades
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-client

