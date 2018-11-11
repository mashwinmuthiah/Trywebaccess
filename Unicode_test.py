import socket

mysock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cdm='GET https://data.pr4.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cdm)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
