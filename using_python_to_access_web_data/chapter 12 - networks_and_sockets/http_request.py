import socket
#connect the socket to port 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
#make a request preparing to sending
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n' .encode()
#send
mysock.send(cmd)
#receive and print the data is receiving
while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mysock.close()