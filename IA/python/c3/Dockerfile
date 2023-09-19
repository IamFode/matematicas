#FROM debian
#LABEL maintainer=@fode
#ARG DEBIAN_FRONTEND=noninteractive
#RUN /bin/bash -c 'source $HOME/.bashrc ; echo $HOME'
#RUN apt-get update --fix-missing && \
#    apt-get install -y \
#    wget bzip2 ca-certificates \
#    libglib2.0-0 libxext6 libsm6 libxrender1
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
#    wget --quiet \
#    https://repo.continuum.io/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh -O /root/miniconda.sh && \
#    /bin/bash /root/miniconda.sh -b -p /opt/conda && \
#    rm /root/miniconda.sh
#ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
#ENV PATH /opt/conda/bin:$PATH
#ENTRYPOINT [ "/usr/bin/tini", "--" ]


# Capitulo 6
#FROM jupyter/base-notebook
#USER root
#RUN conda install --yes numpy pandas
#USER jovyan

# Capitulo 7
#FROM jupyter/scipy-notebook
#USER root
#RUN conda install --name root \
#    pymongo
# instalar bibliotecas a través de pip usando bash y activando el entorno respectivo
#RUN ["bash", "-c", "source activate root && pip install twitter"]
#USER jovyan

#PARA MI COMETIDO
FROM jupyter/scipy-notebook
USER root
RUN conda install --name root \
    numpy \
    pandas \
    matplotlib \
    statsmodels 
RUN ["bash", "-c", "source activate root && pip install ISLP"]
USER jovyan
