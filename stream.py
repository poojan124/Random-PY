import threading
import socket
from time import sleep
import sys
from subprocess import PIPE,STDOUT,Popen

ip = '35.154.186.5'
port = 8002
BUFF_SIZE = 8

sck = socket.socket()
sck.connect((ip,port))

global s
global part
part = b''
def listen(sck):
    global s
    global part
    s = b''
    while True:
        part = sck.recv(8)
        s+=part
       # print("sleep time for listen")
        sleep(1)
        
def printer(stime):
    while True:
        global part
        print(part.decode())
       # print("sleep time for printer")
        sleep(1)

t1 = threading.Thread(target=listen,args=(sck,))
t2 = threading.Thread(target=printer,args=(0.1,))

t1.start()
t2.start()
