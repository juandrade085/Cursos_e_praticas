"""Melhore o jogo do DESAFIO 028 onde o computador vai
'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer."""

from random import randint
from time import sleep  # espera por al
palpite = 0
jogador = 1
computador = 0
print('-*=*' * 13)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-*=*' * 13)
while jogador != computador :
    computador = randint(0, 10)
    jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar
    print('PENSANDO...')
    sleep(2)
    palpite += 1
    if computador == jogador:
        print('Parabéns! Você conseguiu me vencer!!!')
    else:
        print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}.')
print(f'Você precisou de {palpite} palpites pra vencer!!!')