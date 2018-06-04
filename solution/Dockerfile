FROM debian:latest

# =========Install your package=========
RUN apt-get update
RUN apt-get install -y netcat

RUN apt-get install -y python
RUN apt-get install -y gcc
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install pwntools

# ======================================


# ======Build and run your exploit=====
COPY ./SRC/ex.py /bin/exploit
COPY ./SRC/client /bin/client
COPY ./SRC/client /client
RUN chmod 777 /bin/exploit
RUN chmod 777 /bin/client
RUN chmod 777 /client
ENV PWNLIB_NOTERM 1

# Specipy IP address
#ENTRYPOINT ["/usr/bin/python","/bin/ex.py"]
# ======================================
