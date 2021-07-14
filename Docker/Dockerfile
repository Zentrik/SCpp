#FROM nvidia/cudagl:11.4.0-base-ubuntu20.04
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt -y update && \
	apt -y install cmake make git libboost-all-dev build-essential libeigen3-dev libfmt-dev libgtest-dev llvm clang valgrind

WORKDIR /usr/src/googletest
RUN cmake .
RUN cmake --build . --target install
WORKDIR /home

RUN git clone https://github.com/catchorg/Catch2.git
WORKDIR Catch2
RUN mkdir build
WORKDIR build
RUN cmake ..
RUN make 
RUN make install
WORKDIR /home
RUN rm -rf Catch2

#RUN apt -y update && \
#	apt install -y build-essential \
#	libreadline-gplv2-dev \
#	libncursesw5-dev \
#	libssl-dev \
#	libsqlite3-dev tk-dev \
#	libgdbm-dev libc6-dev \
#	libbz2-dev libffi-dev \
#	zlib1g-dev libx11-dev \
#	libxxf86vm-dev \
#	libxcursor-dev \
#	libxi-dev \
#	libxrandr-dev \
#	libxinerama-dev \
#	libglew-dev
#ADD https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz Python-3.7.9.tgz
#RUN tar xzf Python-3.7.9.tgz
#RUN cd Python-3.7.9 && \
#	./configure --enable-optimizations
#RUN cd Python-3.7.9 && \
#	make install

#ADD https://github.com/TylerGubala/blenderpy/releases/download/v2.91a0/bpy-2.91a0-cp37-cp37m-manylinux2014_x86_64.whl bpy-2.91a0-cp37-cp37m-manylinux2014_x86_64.whl
#RUN python3 -m pip install -U pip setuptools wheel
#RUN python3 -m pip install bpy-2.91a0-cp37-cp37m-manylinux2014_x86_64.whl
#RUN bpy_post_install

#RUN rm bpy-2.91a0-cp37-cp37m-manylinux2014_x86_64.whl
#RUN rm -rf Python-3.7.9
#RUN rm Python-3.7.9.tgz