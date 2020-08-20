import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 5000))

msg = s.recv(1024)