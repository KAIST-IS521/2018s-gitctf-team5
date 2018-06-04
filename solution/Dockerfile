FROM debian:latest

# =========Install your package=========
RUN apt update && apt -y upgrade
RUN apt-get update
RUN apt-get install -y make
RUN apt-get install -y gcc
RUN apt-get install -y vim
RUN apt-get install -y xinetd
RUN apt-get install -y libsqlite3-dev
RUN apt-get install netcat -y
RUN apt-get install net-tools -y
RUN apt-get install -y procps
RUN apt-get install -y python python-dev git libssl-dev libffi-dev build-essential
RUN apt-get install -y python-pip
RUN pip install pwntools


# ======Build and run your exploit=====
RUN chmod 777 /
RUN chmod 777 /bin/
ADD ./SRC/gogo.py /bin/exploit
ADD ./SRC/gogo_header.py /bin/gogo_header.py
RUN chmod +x /bin/exploit
RUN chmod +x /bin/gogo_header.py
ENV PWNLIB_NOTERM 1 


# ======Build and run your exploit=====
#WORKDIR /bin/
#ENTRYPOINT ["/bin/exploit", "172.17.0.3", "2001"]
#CMD ["/loop.sh"]
# ======================================




#======original code
#start 
#WORKDIR /root/
#CMD ["/loop.sh"]


