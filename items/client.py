__author__ = 'liyuanpeng'


#!/usr/bin/python

import socket
import time

host = socket.gethostname()
# sock.connect((host,8001))


while True:

    send = raw_input("enter your words: ")

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,8001))
    sock.send(send)

    print 'my recviev: '+sock.recv(1024)

    #if sock.recv(1024) == None:
        #print sock.recv(1024)
     #   print 1
    #else:
     #   print sock.recv(1024)
      #  continue
    if(send=='end'):break

