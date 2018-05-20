##  sudo apt-get install libsqlite3-dev 

## KEY SETTING 
KEY="This ls flag key"

default :
	g++ -std=c++11 ./SRC/client/client.cpp ./SRC/client/main.cpp -o ./SRC/client/client
	g++ -std=c++11 ./SRC/server/server.cpp ./SRC/server/main.cpp -o ./SRC/server/server -lsqlite3
	g++ -std=c++11 ./SRC/server/modify_usr.cpp -o ./SRC/server/modify_usr -lsqlite3
	cp ./SRC/server/server ./BUILD/prob
	cp ./SRC/server/run.sh ./BUILD/run.sh
	cp ./SRC/server/modify_usr ./BUILD/modify_usr
	strip ./BUILD/prob

	echo $(KEY) > ./flag

clean:
	rm ./BUILD/*
	rm ./SRC/server/server
	rm ./SRC/client/client
	rm ./SRC/server/modify_usr
	
