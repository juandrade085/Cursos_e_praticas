"""Faça um mini-sistema que utilize o Interactive Help do
Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores."""
from time import sleep
c = ('\033[m',          # 0 -> sem cores
     '\033[0;30;41m',   # 1 -> vermelho
     '\033[0;30;42m',   # 2 -> verde
     '\033[0;30;43m',   # 3 -> amarelo
     '\033[0;30;44m',   # 4 -> azul
     '\033[0;30;45m',   # 5 -> roxo
     '\033[7;30m',      # 6 -> branco
     )

def pyhelp(comando):
    título(f" Acessando o manual do comando '{comando}'",4)
    print(c[5], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)

def título (msg, cor=0):
    tam = len(msg) + 2
    print(c[cor], end='')
    print(f"{'~' * tam}\n"
          f"{msg}\n"
          f"{'~' * tam}")
    print(c[0], end='')
    sleep(1)

# Programa Principal
while True:
    título('SISTEMA DE AJUDA PyHELP', 3)
    resp = str(input('Função ou Biblioteca > '))
    if resp.upper() == 'FIM':
        break
    else:
        pyhelp(resp)
título(' >>> ATÉ LOGO <<<', 1)