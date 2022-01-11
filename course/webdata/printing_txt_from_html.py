import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

print(mysock.recv(500).decode())  # by defualt .decode() decodingn according to utf8 or ascii character set
# that's why we no need to give .decode('utf8') or .decode('ascii') because it is defualt to .decode()
mysock.close()