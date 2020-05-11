############################################################
# Dockerfile to build GLASSgo Containers
# Based on Ubuntu
# v0.1.0
############################################################

# Set the base image to Ubuntu
FROM ubuntu:19.10

# File Author / Maintainer
LABEL authors="Steffen C. Lott"

# Set the working directory.
WORKDIR /usr/src/GLASSgo

# Set Variables
ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV DEBIAN_FRONTEND noninteractive

# Update the sources list
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y gcc=4:9.2.1-3.1ubuntu1
RUN apt-get install -y python2.7
RUN apt-get install -y python3 wget python3-pip
RUN pip3 install numpy==1.17.4
RUN pip3 install biopython==1.76
RUN apt-get install -y ncbi-blast+=2.8.1-1
RUN apt-get install -y clustalo=1.2.4-2
RUN apt-get install -y bioperl=1.7.2-3
RUN apt-get install -y software-properties-common=0.98.5
RUN apt-get install -y curl=7.65.3-1ubuntu3
RUN apt-get install -y libgsl-dev=2.5+dfsg-6
RUN curl -sL -o/var/cache/apt/archives/viennarna_2.4.14-1_amd64.deb https://www.tbi.univie.ac.at/RNA/download/ubuntu/ubuntu_19_04/viennarna_2.4.14-1_amd64.deb && dpkg -i /var/cache/apt/archives/viennarna_2.4.14-1_amd64.deb

# Copy the application folder inside the container
ADD ./GLASSgo.py .
ADD ./reqPackages/ ./reqPackages/
ADD ./LICENSE .
ADD ./README.md .
ADD ./GLASSgoTestSuite/ ./GLASSgoTestSuite/

# Change Script permissions
RUN chmod +x ./GLASSgo.py
RUN chmod +x ./reqPackages/londen.pl
RUN chmod +x ./GLASSgoTestSuite/GLASSgoTest.py

# Set ENV Variables
ENV PERL5LIB=/usr/src/GLASSgo/reqPackages:$PERL5LIB
