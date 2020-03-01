from socket import *
import random

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    print("Rodando...")
    rand = random.randint(0, 10)

    message, address = server_socket.recvfrom(1024)
    print("Mensagem Recebida: " + message.decode())

    if rand < 4:
        continue

    server_socket.sendto("pong", address)
