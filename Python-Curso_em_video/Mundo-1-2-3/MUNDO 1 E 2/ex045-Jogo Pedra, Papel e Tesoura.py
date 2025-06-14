"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
from time import sleep  # espera por al
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'{' *=* '*8}\n{" JOKENPÔ ":-^40}\n{' *=* '*8}')
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
jogador = int(input('Qual sua jogada? ')) #Jogador tenta adivinhar
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print(f'{' *=* '*8}')
print(f'Computador jogou {itens[computador]}\n'
      f'Jogador jogou {itens[jogador]}')
print(f'{' *=* '*8}')
if computador == 0 : #computador jogou pedra
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1 :
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1 : #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2 : #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
else:
        print('JOGADA INVÁLIDA!')