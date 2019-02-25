import socket

IP = "127.0.0.1"
PORT = 2020

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, PORT))

while True:
    data, addr = s.recvfrom(1024)
    print "received message:", data