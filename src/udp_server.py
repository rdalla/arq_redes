

import socket
import sys
import os
import platform

#_____________________________________________________________

def config():
    global UDP_IP_ADDRESS
    global UDP_PORT_NO

    UDP_IP_ADDRESS = input('Digite o IP do servidor : ')
    UDP_PORT_NO = int(input('Digite a porta desejada entre 10001 e 11000: '))
    while (UDP_PORT_NO < 10001) or (UDP_PORT_NO > 11000):
        print("A porta deve ser entre 10001 - 11000")
        UDP_PORT_NO = int(input('Digite a porta desejada entre 10001 e 11000: '))

    pass
#_____________________________________________________________

def host(UDP_IP_ADDRESS, UDP_PORT_NO):

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    print("Waiting... ")
    data, addr = serverSock.recvfrom(1024)
    data = data.decode()



    #posição do vetor data:
    #ACK = data[0]
    #Message = data[1]
    #MAX_MESSAGE = data[2]

    print("REC: ", data)

    while data[1] < data[2]:
        if data[0] == "0":
            serverSock.sendto(data.encode(), addr)
            print("SENT: ", " ACK = " + data[0] + "\n")

        if data[0] == "1":
            serverSock.sendto(data.encode(), addr)
            print("SENT: ", " ACK = " + data[0] + "\n")

    pass
#_____________________________________________________________

def closeMessage():

    serverSock.close()

    pass

#_____________________________________________________________

def main():

    config()
    host(UDP_IP_ADDRESS, UDP_PORT_NO)
    closeMessage()

#_____________________________________________________________

if __name__ == '__main__':
    main()
