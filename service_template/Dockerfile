FROM debian:latest
MAINTAINER k1rh4 <k1rh4.lee@gmail.com>

###### SERVER SETTING ########
RUN apt-get update 
#RUN apt-get install -y vim 
RUN apt-get install -y xinetd
RUN apt-get install -y libsqlite3-dev
RUN apt-get install netcat -y
RUN apt-get install net-tools -y
RUN apt-get install -y procps
########### USER CREATE #############
RUN useradd -d /home/load load -s /bin/bash
RUN mkdir /home/load


########## HOME DIR SETTING #############
RUN chown -R root:load /home/load
RUN chmod 750 /home/load

###### PROB  SETUP #####
ADD ./BUILD/prob /home/load/
ADD ./BUILD/modify_usr /home/load/modify_usr
ADD ./BUILD/run.sh /home/load/run.sh
ADD ./BUILD/usr.db /home/load/usr.db
RUN chown root:root /home/load/*
RUN chmod 755 /home/load/run.sh
RUN chmod 755 /home/load/modify_usr 
RUN chmod 755 /home/load/prob
RUN chmod 766 /home/load/usr.db

RUN mkdir -p /var/ctf/
COPY ./flag	/var/ctf/flag
RUN chown root:load /var/ctf/flag
RUN chmod 440 /var/ctf/flag


####### XINETD SETTING 
ADD ./SRC/load.xinetd /etc/xinetd.d/load


WORKDIR /home/load
ADD ./SRC/start.sh /start.sh
RUN chmod +x /start.sh 

RUN su load
#ENTRYPOINT /start.sh

#ENTRYPOINT service ssh restart && bash
#ENTRYPOINT /etc/init.d/xinetd retstart && bash


