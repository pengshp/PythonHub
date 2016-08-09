#!/usr/bin/env python3
# socket 客户端构建

import socket

s = socket.socket() #创建socket对象

server = socket.gethostname() #得到当前主机名
port = 1234       #端口号
s.connect((server, port))

print(s.recv(1024))

s.close()
