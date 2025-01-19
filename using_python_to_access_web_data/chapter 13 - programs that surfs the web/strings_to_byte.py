import socket
#connect the socket to port 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
#make a request preparing to sending
# we have a string (unicode) and we encode to bytes(UTF-8)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n' .encode()
# we send to socket
mysock.send(cmd)
#socket receive data in bytes(UTF-8)
# data in bytes(UTF-8) are decoded to string(unicode)
# And print the data decoded
while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mysock.close()