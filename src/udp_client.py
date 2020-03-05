#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os
import platform

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#_____________________________________________________________

def ping_IP(UDP_IP_ADDRESS):
    if platform.system() == "Windows":
        rep = os.system('ping ' + UDP_IP_ADDRESS +" -n 1")
    else:
        rep = os.system('ping -c 3 ' + UDP_IP_ADDRESS)

    while rep != 0:
        print ("Servidor não encontrado...")
        UDP_IP_ADDRESS = input('Digite novamente o IP do servidor : ')
        rep = os.system('ping ' + UDP_IP_ADDRESS)

    pass
#_____________________________________________________________

def config():
    global UDP_IP_ADDRESS
    global UDP_PORT_NO
    global MAX_MESSAGE
    global SEQNO

    UDP_IP_ADDRESS = raw_input('Digite o IP do servidor : ')
    UDP_PORT_NO = int(raw_input('Digite a porta desejada entre 10001 e 11000: '))
    while (UDP_PORT_NO < 10001) or (UDP_PORT_NO > 11000):
        print("A porta deve ser entre 10001 - 11000")
        UDP_PORT_NO = int(raw_input('Digite a porta desejada entre 10001 e 11000: '))

    ping_IP(UDP_IP_ADDRESS)
    print("Servidor Ok!!!")
    MAX_MESSAGE = int(raw_input('Digite o numero maximo de mensagens: '))
    SEQNO = 0

    pass
#_____________________________________________________________

def messenger(UDP_IP_ADDRESS, UDP_PORT_NO, MAX_MESSAGE):
    Message = 0 #começo as mensagens com zero

    while Message < MAX_MESSAGE:

        if SEQNO == 0:
            data = str(SEQNO) + str(Message) + str(MAX_MESSAGE)
            clientSock.sendto(data.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
            print("SENT: ", "SEQNO: " + str(SEQNO) + " / Data: " + str(Message) + " / Maximo: " + str(MAX_MESSAGE))
            try:
                clientSock.settimeout(1.0)
                answer, UDP_IP_ADDRESS = clientSock.recvfrom(1024)
                answer = answer.decode()
                ACK = answer

                if ACK == "0":
                    print("RECV :" + "ACK = " + answer + "\n")
                    SEQNO = 1
                    Message = Message + 1

            except timeout:
                print("RECV: timeout!")

        if SEQNO ==1:
            data = str(SEQNO) + str(Message) + str(MAX_MESSAGE)
            clientSock.sendto(data.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
            print("SENT: ", "SEQNO: " + str(SEQNO) + " / Data: " + str(Message) + " / Maximo: " + str(MAX_MESSAGE))
            try:
                clientSock.settimeout(1.0)
                answer, UDP_IP_ADDRESS = clientSock.recvfrom(1024)
                answer = answer.decode()
                ACK = answer

                if ACK == "1":
                    print("RECV :" + "ACK = " + answer + "\n")
                    SEQNO = 0
                    Message = Message + 1

            except timeout:
                print("RECV: timeout!")

    client_socket.close()


    pass

#_____________________________________________________________

def main():

    config()
    messenger(UDP_IP_ADDRESS, UDP_PORT_NO, MAX_MESSAGE)

#_____________________________________________________________

if __name__ == '__main__':
    main()
