#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os
import platform

#_____________________________________________________________

def config():
    global UDP_IP_ADDRESS
    global UDP_PORT_NO


    UDP_IP_ADDRESS = raw_input('Digite o IP do servidor : ')
    UDP_PORT_NO = int(raw_input('Digite a porta desejada entre 10001 e 11000: '))
    while (UDP_PORT_NO < 10001) or (UDP_PORT_NO > 11000):
        print("A porta deve ser entre 10001 - 11000")
        UDP_PORT_NO = int(raw_input('Digite a porta desejada entre 10001 e 11000: '))

    pass
#_____________________________________________________________

def host(UDP_IP_ADDRESS, UDP_PORT_NO):

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    print("Waiting... ")

    while True:
        data, addr = serverSock.recvfrom(1024)
        data = data.decode()
        print("Message: ", data)

    pass

#_____________________________________________________________

def main():

    config()
    host(UDP_IP_ADDRESS, UDP_PORT_NO, MAX_MESSAGE)

#_____________________________________________________________

if __name__ == '__main__':
    main()
