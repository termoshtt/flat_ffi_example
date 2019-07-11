FROM ubuntu:18.04
LABEL maintainer "Toshiki Teramura <toshiki.teramura@gmail.com>"

RUN apt-get update     \
 && apt-get install -y \
    cmake              \
    g++                \
    libboost-all-dev   \
    libpython3-dev     \
    make               \
    python3-numpy      \
    python3-pip        \
    python3-pytest     \
 && apt-get clean      \
 && rm -rf /var/lib/apt/lists/*
