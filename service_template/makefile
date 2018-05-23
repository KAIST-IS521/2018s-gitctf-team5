##  sudo apt-get install libsqlite3-dev 

## KEY SETTING 
KEY="This_ls_flag_key"
OPTION=-fstack-protector -std=c++11
CC=g++
default :
	$(CC) $(OPTION) ./SRC/client/client.cpp ./SRC/client/main.cpp -o ./SRC/client/client
	$(CC) $(OPTION) ./SRC/server/server.cpp ./SRC/server/main.cpp -o ./SRC/server/server -lsqlite3
	$(CC) $(OPTION) ./SRC/server/modify_usr.cpp -o ./SRC/server/modify_usr -lsqlite3
	cp ./SRC/server/server ./BUILD/prob
	cp ./SRC/server/run.sh ./BUILD/run.sh
	cp ./SRC/server/usr.db ./BUILD/usr.db
	cp ./SRC/server/modify_usr ./BUILD/modify_usr
	strip ./BUILD/prob
	strip ./BUILD/modify_usr

	#echo $(KEY) > ./flag

clean:
	rm ./BUILD/*
	rm ./SRC/server/server
	rm ./SRC/client/client
	rm ./SRC/server/modify_usr
	
