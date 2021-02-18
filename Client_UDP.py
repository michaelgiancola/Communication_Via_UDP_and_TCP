'''Author: Michael Giancola
 *Date: 24/10/2019
 *Description: This file contains part of a UDP application where a UDP Client sends ASCII requests to UDP Server
 '''

from socket import *                                            #includes all packages within the socket package

UDP_IP = '127.0.0.1'                                            #the loopback adapter address; used to test communication on my local network
UDP_PORT = 5005                                                 #chosen allowable arbitrary port for communication

clientS = socket(AF_INET, SOCK_DGRAM)                           #creates a UDP socket for server; notice SOCK_DGRAM indicates UDP protocol

message = input("Please enter your command: ")                  #Prompts user to use keyboard to input a command and stores it in message variable; input is a built-in function in Python for user input
clientS.sendto(message.encode(), (UDP_IP, UDP_PORT))            #client sends encoded message that was inputted to the loopback address and specified port

returnMessage, serverAddress = clientS.recvfrom(4096)           #when a packet arrives from Internet at the client's socket the packet data is stored in returnMessage and the serverAddress contains the server's port number and IP; 4096 is a standard number for message length in bytes   
print(returnMessage.decode())                                   #prints the decoded message so that it is in easily readable format







