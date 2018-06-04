#!/bin/bash
###############################################################################
# Git-based CTF
###############################################################################
#
# Author: SeongIl Wi <seongil.wi@kaist.ac.kr>
#         Jaeseung Choi <jschoi17@kaist.ac.kr>
#         Sang Kil Cha <sangkilc@kaist.ac.kr>
#
# Copyright (c) 2018 SoftSec Lab. KAIST
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



if [ "$#" -ne 3 ]; then
    echo "Usage: $0 [exploit name] [ip] [port]"
    exit 1
fi

EXPLOITNAME=$1
IP=$2
PORT=$3

docker build -t $EXPLOITNAME .
docker run -it --rm --net="host" --name $EXPLOITNAME \
                --entrypoint "/bin/exploit" $EXPLOITNAME $IP $PORT


#docker run -it --rm --net="host" --name $EXPLOITNAME --entrypoint "/bin/exploit $IP $PORT" $EXPLOITNAME
#docker run --entrypoint /bin/exploit $EXPLOITNAME $IP $PORT -it --rm --net="host" --name $EXPLOITNAME
#docker run --rm --name $EXPLOITNAME -i -d -t $EXPLOITNAME --entrypoint debian latest /bin/gogo.py $IP $PORT
# it works!
#docker run --net="host" -it --rm $EXPLOITNAME  bash;
#docker run --net="host" -it --rm $EXPLOITNAME  bash;

