# GPU or CPU only
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    wget \
    unzip \
 && rm -rf /var/lib/apt/lists/*

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8


# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh
RUN bash Miniconda3-py37_4.8.2-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-py37_4.8.2-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

RUN conda install -y python=3.7.3
RUN conda install -y pytorch==1.4.0 cudatoolkit=10.0 -c pytorch
RUN conda install faiss-gpu cudatoolkit=10.0 -c pytorch


#Install Cython
RUN apt-get update
RUN apt-get -y install --reinstall build-essential
RUN apt-get -y install gcc
RUN conda install -y -c conda-forge cython

#Install LASER
RUN git clone https://github.com/facebookresearch/LASER.git
ENV LASER=/LASER
RUN bash /LASER/install_models.sh
RUN bash /LASER/install_external_tools.sh

#Create work environement
RUN mkdir /embeddings
RUN mkdir /input
RUN mkdir /output
WORKDIR /workdir

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "create_embeddings.py"]