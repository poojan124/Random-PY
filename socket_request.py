import socket

ip = '35.154.186.5'
port = 8100
BUF_SIZE = 4096

def recv_all(sck,response):
    chunk = sck.recv(BUF_SIZE)
    respongse += chunk
    if len(chunk)<BUF_SIZE:
        return response
    else:
        return  recv_all(sck,response)

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect((ip,port))

s = b'''GET / HTTP/1.1
Host: 35.154.186.5:8100
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
'''
ss = b'GET / HTTP/1.1\r\n\r\n'

sck.send(s)

res = sck.recv(10000)
print(res)
res = sck.recv(10000)
print(res)
print(type(res))
