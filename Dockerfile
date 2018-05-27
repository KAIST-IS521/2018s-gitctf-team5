FROM debian:latest

###### SERVER SETTING ########
RUN apt-get update
#RUN apt-get install -y vim
RUN apt-get install -y xinetd
RUN apt-get install -y libsqlite3-dev
RUN apt-get install -y sqlite3

###### PROB  SETUP #####
ADD ./BUILD/prob /prob
ADD ./BUILD/usr.db /usr.db
RUN mkdir -p /var/ctf/
COPY ./flag	/var/ctf/flag
####### XINETD SETTING

ENTRYPOINT ["./prob","4000","."]
#ENTRYPOINT service ssh restart && bash


