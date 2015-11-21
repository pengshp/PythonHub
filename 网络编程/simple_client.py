#!/usr/bin/env python3
#socket 客户端构建

import socket

s=socket.socket()

server=socket.gethostname()
port=1234
s.connect((server,port))

print (s.recv(1024))

s.close()

