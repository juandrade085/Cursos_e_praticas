"""Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário em
Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado."""
from random import randint
from time import sleep
from operator import itemgetter

pos = 0
print(f'Valores sorteados:')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('-='*15)
print(jogo)
print('-='*15)
for k, v in jogo.items():
    print(f'    O {k} tirou {v};')
    sleep(0.5)
print('-='*15)
jogo_ordenado = dict()
jogo_ordenado = sorted(jogo.items(), key=itemgetter(1), reverse= True)
print('-='*15)
print(jogo_ordenado)
print('-='*15)
print('Ranking dos jogares:')
for i, v in enumerate(jogo_ordenado):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(0.5)
