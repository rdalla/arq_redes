from socket import socket, AF_INET, SOCK_DGRAM, timeout
import sys
import os
import platform

global ipServer
global port
global maxMessage


#https://www.cybrary.it/blog/0p3n/ping-using-python-script/
def ipConfig():
	while True:
		ipServer = input('Digite o IP do servidor : ')

		if platform.system() == "Windows":
			rep = os.system('ping ' + ipServer +' -n 1')
			print ("Servidor Ok!!!")
			break
		else:
			rep = os.system('ping -c 2 ' + ipServer)
			print ("Servidor Ok!!!")
			break

		while rep != 0:
			print ("Servidor não encontrado...")
			ipServer = input('Digite novamente o IP do servidor : ')
			if platform.system() == "Windows":
				rep = os.system('ping ' + ipServer +' -n 1')
			else:
				rep = os.system('ping -c 2 ' + ipServer)
	return ipServer


def portConfig():
	while True:
		port = int(input('Digite a porta entre 10001 e 11000: '))

		while (port < 10001) or (port > 11000):
			print("A porta deve ser entre 10001 - 11000")
			port = int(input('Digite a porta desejada entre 10001 e 11000: '))
		print ("Porta válida")
		break
	return port


def maxMessage():
	MAX_MESSAGE = input('Digite o numero maximo de mensagens: ')

	while True:
		try:
			MAX_MESSAGE = int(MAX_MESSAGE)
			break
		except:
			print("O valor deve ser um numero inteiro")
			MAX_MESSAGE = input('Digite novamente o numero maximo de mensagens: ')
	return MAX_MESSAGE

def sender():
	ipServer = ipConfig()
	port = portConfig()
	MAX_MESSAGE = maxMessage()
	destiny = (ipServer,port)

	client_socket = socket(AF_INET, SOCK_DGRAM)

	seqno = 0
	data = 1

	while (data < MAX_MESSAGE):
		if seqno == 0:
			message = str(seqno) + str(data) + str(MAX_MESSAGE)
			client_socket.sendto(message.encode(), destiny)
			print("SENT: " + str(seqno) + str(data) + str(MAX_MESSAGE))
			try:
				client_socket.settimeout(1)
				resp, ipServer = client_socket.recvfrom(2048)
				resp = resp.decode()
				ACK = resp[3]
				if ACK == "0":
					print("RECV: " + resp + "\n")
					seqno = 1
					data = data + 1

			except timeout:
				print("RECV: Timeout")

		if seqno == 1:
			message = str(seqno) + str(data) + str(MAX_MESSAGE)
			client_socket.sendto(message.encode(), destiny)
			print("SENT: " + str(seqno) + str(data) + str(MAX_MESSAGE))
			try:
				client_socket.settimeout(1)
				resp, ipServer = client_socket.recvfrom(2048)
				resp = resp.decode()
				ACK = resp[3]
				if ACK == "1":
					print("RECV: " + resp + "\n")
					seqno = 0
					data = data + 1

			except timeout:
				print("RECV: Timeout")
	client_socket.close()

sender()
