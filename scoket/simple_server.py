#!/usr/bin/env python3
#socket 服务器构建

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(10)

while True:
    c,addr=s.accept()                    #接受一个连接
    print ('Get connection from ',addr)
    c.send('This is a simple server'.encode())    #发送数据
    c.close()                            #关闭连接
