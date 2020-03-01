import sys, time
from socket import *

server_port = 12000

# Receber IP do server como argumento de linha de comando
argv = sys.argv
server_ip = argv[1]

timeout = 1 # 1 segundo

# Criar socket cliente
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(timeout)

ping_id = 0

# ping 10 vezes
while ping_id < 10:
    ping_id += 1

    try:

        rtt_init = time.time()
        client_socket.sendto("ping".encode(), (server_ip, server_port))
        message, address = client_socket.recvfrom(1024)
        rtt_end = time.time()

        print("Resposta do servidor: " + server_ip + ": " + message.decode() 
                                        + " RTT: " + str(rtt_end - rtt_init))
    except:
        print("Timeout")
        continue

client_socket.close()
