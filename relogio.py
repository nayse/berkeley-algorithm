import socket
from random import randint
import time
from datetime import datetime


SERVIDOR_HOST = 'localhost'
SERVIDOR_PORTA = 5000

def obter_tempo_atual():
    #retorna o tempo atual em segundos
    return time.time() + randint(1000, 3000)

def main():
    #cria o socket cliente e se conecta ao servidor
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco_servidor = (SERVIDOR_HOST, SERVIDOR_PORTA)
    socket_cliente.connect(endereco_servidor)

    
    tempo_atual = obter_tempo_atual()
    print(f"A hora atual do cliente é: {datetime.fromtimestamp(tempo_atual).time().isoformat('seconds')}")
    time.sleep(2)

    print("\n")
    print("O tempo do relógio atual foi enviado para o servidor!")
    #envia o tempo atual para o servidor
    socket_cliente.sendall(str(tempo_atual).encode())
    print("\n")

    dados = socket_cliente.recv(1024) #socket do relogio recebe a hora ajustada 
    tempo_ajustado = float(dados.decode()) 
    
    tempo_atual = tempo_ajustado
    time.sleep(1)
    print(f"Tempo ajustado: {datetime.fromtimestamp(tempo_atual).time().isoformat('seconds')}")

    socket_cliente.close()

if __name__ == '__main__':
    main()
