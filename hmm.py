import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "192.168.76.95", 12345
s.bind((host, port))
s.listen(5)
c, addr = s.accept()

c.send(b"Thank you for connecting to my server")
print(c.recv(1024))
c.close()
