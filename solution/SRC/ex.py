#!/usr/bin/env python

from pwn import process
import logging

import sys
import time

HOST = sys.argv[1]
logging.getLogger().disabled=True
PORT = sys.argv[2]
KEY="";
p = process(["./client",HOST,PORT],level='error')
p.recvuntil("username:");
p.sendline("admin")
p.recvuntil("password:");
p.sendline("t34m5");

KEY = p.recv(timeout=3)


flag = KEY
flag = flag.rstrip()
sys.stdout.write(flag)
