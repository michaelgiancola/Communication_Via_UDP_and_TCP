'''Author: Michael Giancola
 *Date: 24/10/2019
 *Description: This file contains part of a TCP application where a TCP Client connects and sends ASCII requests to TCP Server
 '''

from socket import *                                               #includes all packages within the socket package

TCP_IP = '127.0.0.1'                                               #the loopback adapter address; used to test communication on my local network
TCP_PORT = 5005                                                    #chosen allowable arbitrary port for communication

clientS = socket(AF_INET, SOCK_STREAM)                             #creates a TCP socket for server; notice SOCK_STREAM indicates TCP protocol
clientS.connect((TCP_IP, TCP_PORT))                                #for a client to send data to server, a connection must be established first between client and server, this line initiates the TCP connection
print("Connection to Server Established...")                       #print to show that the connection to the server has been made 

message = input("Please enter your command: ")                     #Prompts user to use keyboard to input a command and stores it in message variable; input is a built-in function in Python for user input
clientS.sendall(message.encode())                                  #client sends encoded message that was inputted, to the TCP server it made a connection with

returnMessage = clientS.recv(4096)                                 #when a packet arrives from Internet at the client's socket the packet data is stored in returnMessage; 4096 is a standard number for message length in bytes   
print(returnMessage.decode())                                      #prints the decoded message so that it is in easily readable format

clientS.close()                                                    #client is finished sending requests so the TCP connection is closed between the client and server
