"""Escreva um programa que faça o computador "pensar" em
um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário acertou ou não."""
from random import randint
from time import sleep  # espera por al
n = randint(0, 5)
print('-*=*' * 13)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-*=*' * 13)
num = int(input('Em que número pensei? ')) #Jogador tenta adivinhar
print('PENSANDO...')
sleep(2)
if n == num:
    print('Parabéns! Você conseguiu me vencer!!!')
else:
    print(f'Ganhei! Eu pensei no número {n} e não no {num}.')
