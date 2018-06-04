#!/usr/bin/python

from pwn import *
from struct import *
from os import *
import socket


def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


def dologin(r):
        r.send("user test\r\npass test\r\n")
        r.recvuntil('230 Login successful.')

def portModeSend(r, dport):
        localip = get_ip_address().replace('.',',')
        l = listen(dport,level='error') # listen port for data
        payload  = ""
        payload += "port "
        payload += localip
        payload += ",{},{}".format(dport/256,dport%256)
        payload += "\r\n"
        r.send(payload)
        r.recvuntil('200 port command successful.')
        return l

def doPut(r):
        payload  = ""
        payload += "stor "
        payload += "file"
        payload += "\r\n"
        r.send(payload)
        r.recvuntil('150 ok to send data.')

def sendData(r, l, size, data):
        l.sendline(p32(size) + data)
        r.recvuntil('226 Transfer complete.')

def doGet(r):
        payload  = ""
        payload += "retr "
        payload += "file"
        payload += "\r\n"
        r.send(payload)
        r.recvuntil('150 Opening data connection for file. Please wait...')
        r.recv(1000,timeout=1)
        print "Waiting for server reply.. (1/3) "
        r.recv(1000,timeout=1)
        print "Waiting for server reply.. (2/3)"
        r.recv(1000,timeout=1)
        print "Waiting for server reply.. (3/3)"

def getData(r, l, size):
        recv_data = l.recv(size, timeout=10)
        r.recvuntil('226 Transfer complete.')
        return recv_data
