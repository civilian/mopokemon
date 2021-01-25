FROM ubuntu:18.04 as base

# When dealing with really hard bugs PYTHONUNBUFFERED allows you not to buffer stdin and stdout so it gives more realible logs to know the order of execution
# The debugger does not work if this environment variable is not set
ENV PYTHONUNBUFFERED=1

RUN apt-get update

RUN apt-get -y install software-properties-common

RUN apt-get -y install python3.8

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

RUN apt-get -y install python3-pip

# RUN apt-get -y install postgresql

# RUN apt-get -y install python-psycopg2

# To fix Python.h includes and compilations

RUN apt-get -y install python3.8-dev

FROM base as with-requirements

ENV BASE_DIR=/mopokemon

WORKDIR $BASE_DIR

COPY requirements.txt $BASE_DIR/

RUN pip3 install -r requirements.txt

