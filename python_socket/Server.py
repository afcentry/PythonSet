#coding:utf-8
"""
Author:afcentry
DateTime:2018/08/24
"""

import socket

ip_port = ('127.0.0.1',20000)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting...')
    conn,addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data)
    conn.sendall(b'Receive Datas from client...')

    conn.close()