'''Author: Michael Giancola
 *Date: 24/10/2019
 *Description: This file contains part of a TCP application where a TCP Server processes and responds to TCP Client
 '''

from socket import *                           #includes all packages within the socket package
from datetime import datetime                  #includes datetime package for retreiving the current date and time

TCP_IP = '127.0.0.1'                           #the loopback adapter address; used to test communication on my local network
TCP_PORT = 5005                                #chosen allowable arbitrary port for communication

serverS = socket(AF_INET, SOCK_STREAM)         #creates a TCP socket for server; notice SOCK_STREAM indicates TCP protocol
serverS.bind((TCP_IP, TCP_PORT))               #binds the port number 5005 to the server's socket;
serverS.listen(1)                              #wait and listen for TCP connection requests from client, the parameter specifies the max number of queued connections (at least 1)

print("Server listening...")                   #print statement to indicate the server is listening

while True:                                                                                             #allows TCPServer to connect with Client, receive and process packets from clients continuously and then closes connection when communication is complete
    conn, clientAddr = serverS.accept()                                                                 #when a client requests to connect wth server, a new socket is created called conn (connection socket) which is dedicated to this particular client
    message = conn.recv(4096)                                                                           #when a packet arrives at server's socket, the packet's data is put into varaible message; 4096 is a standard number for message length in bytes  
    if (message.decode() == "What is the current date and time?"):                                      #if the client sends this specific ASCII request, do the following; decodes message
        current = datetime.now()                                                                        #current gives you the date and time information at the current instant
        year = current.strftime("%Y")                                                                   #strftime allows you to format and parse the information and only the year is stored in the variable
        month = current.strftime("%m")                                                                  #strftime allows you to format and parse the information and only the month is stored in the variable
        day = current.strftime("%d")                                                                    #strftime allows you to format and parse the information and only the day is stored in the variable
        time = current.strftime("%H:%M:%S")                                                             #strftime allows you to format and parse the information and only the time is stored in the variable
        returnMessage = "Current Date and Time - " + month + "/" + day + "/" + year + " " + time        #appropriately formatted date and time is stored in variable
        conn.sendall(returnMessage.encode())                                                            #returnMessage is now encoded and sent to the client who sent the request
    else:
        returnMessage = "Invalid Request!"                                                              #if the message sent from the client is not the above, this return message is sent
        conn.sendall(returnMessage.encode())                                                            #sends above message to specific client through the connection socket
    conn.close()                                                                                        #closes the connecton socket so that other clients are able to connect with this TCP Server and send requests

    

        
		




