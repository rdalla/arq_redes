# Arq_Redes
# Projeto I – Transporte confiável de dados utilizando protocolo de bit alternante

O projeto é dividido entre dois arquivos principais:

# udp_client.py : 
É o mensageiro de dados onde existe predeterminado uma sequencia de informação (SEQNO DATA MAX_MESSAGE) para testar o protocolo bit alternante, onde a cada transmissão alterno o bit SEQNO para que o dado DATA seja retransmitido para o servidor somando +1 e farei este fluxo de dados até atingir o MAX_MESSAGE.

# udp_server.py: 
É o servidor de dados onde receberá a informação do mensageiro e verificará o ACK bit (SEQNO) para retransmitir "ACK0" ou "ACK1", desta forma isto fará a alternância do SEQNO bit no client.


# Como testar:
0.  Clone o repositório do projeto.
1.  Descubra o IP da sua maquina no terminal de comandos (ipconfig - Windows ou ifconfig - Linux) 
2.  Abra o udp_client.py no terminal >>> "python3 udp_client.py"
3.  Insira o IP da sua maquina
4.  Insira a porta desejada (entre 10001 a 11000)
5.  Insira a quantidade máxima de mensagens. (por exemplo: 5 mensagens)
6.  Após isso, o protocolo de bit alternante irá processar a informação do cliente para o servidor.
7.  Irá executar o fluxo de dados enquanto (DATA > MAX_MESSAGE).
8.  Após ultrapassar a condição irá fechar a conexão.
