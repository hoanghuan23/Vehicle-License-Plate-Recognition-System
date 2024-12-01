FROM ubuntu
WORKDIR /SRC
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-tk

COPY front_end.py ./front_end.py