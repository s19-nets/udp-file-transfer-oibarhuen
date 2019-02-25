
#The socket will be imported
import socket


#The following two lines, determines the address in which connection between server and client will take place
IP = "127.0.0.1"
PORT = 2020


#The following line is the socket which is the method to connect the two nodes through the address and port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, PORT))


#Lastly, the last lines confirm in the incoming data comes within the byte's limit and will deliver a confirmation.
while True:
    data, addr = s.recvfrom(1000)
    print "received message:", data