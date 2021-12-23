import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ip = '127.0.0.1'
# mysock.connect((ip, 80))
# cmd = 'GET http://127.0.0.1:5500/index.html HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# print(mysock.recv(500).decode())
# mysock.close()

ip = socket.gethostbyname('http://127.0.0.1:5500')
print(ip)
