

from socket import socket, AF_INET, SOCK_DGRAM, timeout
import sys
import os
import platform

#_____________________________________________________________

def config():
    global UDP_PORT_NO

    UDP_PORT_NO = int(input('Digite a porta desejada entre 10001 e 11000: '))
    while (UDP_PORT_NO < 10001) or (UDP_PORT_NO > 11000):
        print("A porta deve ser entre 10001 - 11000")
        UDP_PORT_NO = int(input('Digite a porta desejada entre 10001 e 11000: '))

    pass
#_____________________________________________________________

def host(UDP_PORT_NO):
    Message = 0 #Apenas para inicialização
    MAX_MESSAGE = 1 #Apenas para inicialização

    serverSock = socket(AF_INET, SOCK_DGRAM)
    serverSock.bind(('', UDP_PORT_NO))
    print("Waiting... ")
    while Message < MAX_MESSAGE:
        data, addr = serverSock.recvfrom(1024)
        data = data.decode()

        Message = int(data[1])
        MAX_MESSAGE = int(data[2])

        print("REC: ", data)

        if data[0] == "0":
            serverSock.sendto("ACK0".encode(), addr)
            print("SENT: ACK0 \n")
        if data[0] == "1":
            serverSock.sendto("ACK1".encode(), addr)
            print("SENT: ACK1 \n")

    serverSock.close()
    pass

#_____________________________________________________________

config()
host(UDP_PORT_NO)
