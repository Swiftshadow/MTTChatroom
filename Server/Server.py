import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# connect to yourself
# uses port 42069
s.bind((socket.gethostname(), 5000))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established")
    client_socket.send(bytes("Welcome to the server!", "utf-8"))
