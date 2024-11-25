FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y udev systemctl wget usbutils

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libusb-1.0-0-dev \
    git \
    cmake

# Install optional packages
RUN apt-get update && apt-get install -y \
    freeglut3-dev \
    libxmu-dev \
    libxi-dev \
    libglib2.0-0

RUN pip3 install numpy==2.1.2 cython

WORKDIR /workspace

