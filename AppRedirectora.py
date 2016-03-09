#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

#creamos el socket
#Se lee así: del modulo socket utiliza el metodo socket (socket.socket)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        print recvSocket.recv(1024)
        NUMaleatorio = random.randint(0, 1000000000)
        recvSocket.send("HTTP/1.1 302 Found\r\n\r\n" +
                        "<html><head>" +
                        '<meta http-equiv="refresh" content="0;url=http://localhost:1235" />' +
                         "</head><html>"+ "\r\n")
        recvSocket.close()

except KeyboardInterrupt:
    print "Closing binded socket"
    mysocket.close()
