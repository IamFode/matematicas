FROM debian
LABEL maintainer=@fode
ARG DEBIAN_FRONTEND=noninteractive
RUN /bin/bash -c 'source $HOME/.bashrc ; echo $HOME'
RUN apt-get update --fix-missing && \
 apt-get install -y \
 wget bzip2 ca-certificates \
 libglib2.0-0 libxext6 libsm6 libxrender1
