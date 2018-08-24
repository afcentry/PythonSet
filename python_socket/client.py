#coding:utf-8
"""
Author:afcentry
DateTime:2018/08/24
"""

import socket
from  time import sleep
ip_port = ('127.0.0.1',20000)

sk = socket.socket()
sk.connect(ip_port)


sk.sendall(b'requesting...')

server_reply = sk.recv(1024)
print(server_reply)

sk.close()