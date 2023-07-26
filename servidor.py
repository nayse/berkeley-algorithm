import socket
from threading import Thread
from random import randint
import time
from datetime import datetime


SERVIDOR_HOST = 'localhost'
SERVIDOR_PORTA = 5000


relogios = []
quantidade_relogios = 3

tempo_atual = time.time() + randint(1000, 3000) #gera valor do tempo inicial p/ servidor

def calcular_media(): #calcula a média dos tempos recebidos dos relógios/clientes.
    tempos = [] #recebe os dados enviados pelo relógio/cliente
    for relogio in relogios:
        dados = relogio.recv(1024)
        tempos.append(float(dados))
    tempos.append(float(tempo_atual))
    media = sum(tempos) / len(tempos)
    return media

def transmitir_media(media): #envia a média para todos os relógios/clientes conectados.
    global tempo_atual
    tempo_atual = media 
    for relogio in relogios:
        mensagem = str(media).encode()
        relogio.sendall(mensagem)
    time.sleep(1)

    print("\n")
    print(f"Os relógios foram ajustados! Hora depois do ajuste: {datetime.fromtimestamp(tempo_atual).time().isoformat('seconds')}")
    print("\n")

def main():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((SERVIDOR_HOST, SERVIDOR_PORTA))
    socket_servidor.listen()
    print(f"Servidor em execução {SERVIDOR_HOST}:{SERVIDOR_PORTA}")

    time.sleep(1)
    print("\n")
    print(f"Hora atual do servidor: {datetime.fromtimestamp(tempo_atual).time().isoformat('seconds')}")
    print("\n")

    while True:
        relogio, endereco = socket_servidor.accept()
        relogios.append(relogio)
        
        print(f"Conexão sucedida com o relógio: {endereco}")
        print("/n")

        if len(relogios) == quantidade_relogios:
            media_tempos = calcular_media()
            transmitir_media(media_tempos)
            break

if __name__ == "__main__":
    main()
