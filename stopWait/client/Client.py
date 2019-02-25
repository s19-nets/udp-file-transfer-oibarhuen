
from socket import *
import socket
import sys

Port = 2020
IP = "127.0.0.1"


s = socket.socket(AF_INET, SOCK_DGRAM)


print ("Connection successfull")


msg = input ('Enter message or data to send as a string: ')

s.sendto(msg, (IP, Port))


data = s.recvfrom(1024)
reply = data[0]
addr = data[1]

print ( + reply.decode())


print ('Error sending message ' )
sys.exit()

