'''Author: Michael Giancola
 *Date: 24/10/2019
 *Description: This file contains part of a UDP application where a UDP Server processes and responds to UDP Client
 '''
 
from socket import *                 #includes all packages within the socket package
from datetime import datetime        #includes datetime package for retreiving the current date and time

UDP_IP = '127.0.0.1'                 #the loopback adapter address; used to test communication on my local network
UDP_PORT = 5005                      #chosen allowable arbitrary port for communication

serverS = socket(AF_INET, SOCK_DGRAM)   #creates a UDP socket for server; notice SOCK_DGRAM indicates UDP protocol
serverS.bind((UDP_IP, UDP_PORT))        #binds the port number 5005 to the server's socket

print("Server can now receive messages") #print statement

while True:                                                                                         #allows UDPServer to receive and process packets from clients continuously
    message, clientAddress = serverS.recvfrom(4096)                                                 #when a packet arrives at server's socket, the packet's data is put into varaible message and its source address is put in clientAddress; 4096 is a standard number for message length in bytes 
    if (message.decode() == "What is the current date and time?"):                                  #if the client sends this specific ASCII request, do the following; decodes message
        current = datetime.now()                                                                    #current gives you the date and time information at the current instant
        year = current.strftime("%Y")                                                               #strftime allows you to format and parse the information and only the year is stored in the variable
        month = current.strftime("%m")                                                              #strftime allows you to format and parse the information and only the month is stored in the variable  
        day = current.strftime("%d")                                                                #strftime allows you to format and parse the information and only the day is stored in the variable
        time = current.strftime("%H:%M:%S")                                                         #strftime allows you to format and parse the information and only the time is stored in the variable
        returnMessage = "Current Date and Time - " + month + "/" + day + "/" + year + " " + time    #appropriately formatted date and time is stored in variable
        serverS.sendto(returnMessage.encode(), clientAddress)                                       #returnMessage is now encoded and sent to the source address
    else:                                   
        returnMessage = "Invalid Request!"                                                          #if the message sent from the source is not the above, this return message is sent
        serverS.sendto(returnMessage.encode(), clientAddress)                                       #sends above message to source address
        
		




