"""Crie um jogo de adivinhação: o programa deve escolher
um número aleatório entre 1 e 50 (use a biblioteca random) e o usuário
deve tentar adivinhar. O programa continua pedindo até que o usuário
acerte."""

from random import randint
from time import sleep
tentativas = 0
jogador = 1
maquina = randint(1, 50)

print(f"{'*-'*20}\n{' Estou pensando em um número ':.^40}\n"
      f"{' Tente adivinhar ':^40}\n"
      f"{' DICA: Está entre 1 e 50 ':.^40}\n{'*-'*20}")
while True:
    jogador = int(input('Em qual número estou pensando...?\n'
                        '>>>'))
    print('PENSANDO...🤔')
    sleep(1)
    print('🤔')
    sleep(1)
    print('🤔')
    sleep(1)
    tentativas += 1
    if maquina > jogador :
        print(f"😛GANHEI!😛\nChute mais alto...")
    elif maquina < jogador :
        print(f"😛GANHEI!😛\nChute mais baixo...")
    if jogador == maquina:
        print(f"🎉🎉🎉PARABÉNS!🎉🎉🎉\nVOCÊ CONSEGUIU ME VENCER!\n"
              f"Você precisou de {tentativas} tentativas pra me vencer!")
        break
print('\nVOLTE SEMPRE 👋😄')