import platform
import multiprocessing
import psutil
import threading
from datetime import datetime
from time import sleep
import os
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW(f'Informações da máquina {platform.node()}')
giga=(1024 ** 3)
delay=20
fechar = False
#os.system(f'Informações da máquina {platform.node()}')

def MaquinaAtual():
    print("Informações da máquina:")
    print(f"Nome da Máquina: {platform.node()}")
    print(f"Sistema Operacional: {platform.system()} Versao {platform.release()}")
    print(f"Arquitetura do processador: {platform.machine()}")
    print(f"Processador: {platform.processor()}")
    print(f"Quantidade de Núcleos: {multiprocessing.cpu_count()}")
    print(f"Quantidade de Threads: {len(multiprocessing.active_children())}")
    print(f"Quantidade Total de Memória: {round((psutil.virtual_memory().total)/giga,3)} Gigabytes")
    print(f"Quantidade de Memória Usada: {round((psutil.virtual_memory().used)/giga,3)} Gigabytes")
    print(f"Porcentagem de Uso de Memória: {round(psutil.virtual_memory().percent,3)}%")
    print("Porcentagem de Uso dos Processadores:")
    for i, porcentagem in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
        print(f"Processador {i+1}: {porcentagem}%")



def limpar_tela():
    if os.name == "posix":
        # Limpar a tela em sistemas tipo Unix (Linux, macOS)
        os.system("clear")
    elif os.name == "nt":
        # Limpar a tela no Windows
        os.system("cls")


def input_com_temporizador_simples(frase):
    resposta=None
    def leitura():
        global delay,fechar
        nonlocal resposta
        print(f'{frase}')
        print(f'Hora Atual: {datetime.now().strftime("%H:%M")}')
        resposta = input("Feche o programa: ")
        if resposta is None or not resposta.isdigit():
            fechar=True
        else:
            delay = int(resposta)
            print(f'Taxa de atualização definida para {delay} segundos.')

    t = threading.Thread(target=leitura)
    t.start()
    sleep(0.1)
    t.join(delay)  # Aguarda a thread pelo tempo especificado




fala = 'Digite taxa de atualizacao em segundos para programa:' \
           '\nValor que nao seja numero para fechar programa'

while True:
    limpar_tela()
    MaquinaAtual()
    input_com_temporizador_simples(fala)
    if fechar:
        break

