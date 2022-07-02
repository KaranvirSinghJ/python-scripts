import socket
import sys
from xmlrpc.client import _HostType

def socket():
    try:
        global host 
        global port 
        global s 
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        
