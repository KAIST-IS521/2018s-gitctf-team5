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
    echo "Usage: $0 [repository URL] [port number]"
    exit 1
fi
LOGFILE=log.txt
URL=$1
PORT=$2

# Parse repository name assuming URL = (any character)/[Repository Name].git
REPONAME=${URL##*/}
PROJNAME=${REPONAME%.*}
SETUPFILE=./setup.sh

rm -f $LOGFILE
touch $LOGFILE
rm -rf $PROJNAME

### 1. CLONE
echo "[*] Clone $URL" >> $LOGFILE
git clone $URL
if [[ $? != 0 ]]; then
    echo "[*] Clone failed." >> $LOGFILE
    exit 1
fi

### 2. SETUP
pushd $PROJNAME

if [ ! -f $SETUPFILE ]; then
    popd
    echo "[*] $SETUPFILE file does not exist." >> $LOGFILE
    exit 1
fi

$SETUPFILE $PROJNAME $PORT
if [ $? -ne 0 ]; then
    echo "[*] Docker setup failed for $PROJNAME." >> ../$LOGFILE
    popd
    exit 1
fi

popd

### 3. Check the liveness
if [[ $(lsof -i -P -n | grep $PORT) ]]; then
    echo "[*] $PROJNAME service is succussfully running." >> $LOGFILE
else
    echo "[*] $PROJNAME service is not running." >> $LOGFILE
fi

docker kill $PROJNAME
docker rm -f $PROJNAME
rm -rf $PROJNAME
