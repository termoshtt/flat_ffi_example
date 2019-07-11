FROM ubuntu:18.04
LABEL maintainer "Toshiki Teramura <toshiki.teramura@gmail.com>"

RUN apt-get update \
 && apt-get install -y \
    cmake          \
    g++            \
    libboost-dev   \
    libpython3-dev \
    make           \
    python3-numpy  \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
