
from socket import *
import socket
import sys


#The following two lines, determines the address in which connection between server and client will take place
Port = 2020
IP = "127.0.0.1"

#The following line is the socket which is the method to connect the two nodes through the address and port will call it s
s = socket.socket(AF_INET, SOCK_DGRAM)

#this line will confirm connection from the client's side
print ("Connection successfull")

#this line will ask the client for the data that will be send
msg = input ('Enter message or data to send as a string (limit of 1000 bytes): ')

#will send data through the connection
s.sendto(msg, (IP, Port))

#Will determine the data's bytes
data = s.recvfrom(1000)
reply = data[0]
addr = data[1]

print ( + reply.decode())


print ('Error sending message ' )
sys.exit()

