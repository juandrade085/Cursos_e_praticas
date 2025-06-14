"""Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário em
Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado."""
from random import randint
from time import sleep
jogo = dict()
pos = 0
print(f'Valores sorteados:')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'    O {k} tirou {v};')
    sleep(0.5)
print('-='*15)
jogo_ordenado = dict(sorted(jogo.items(), key=lambda item: item[1], reverse= True))
print('Rancking dos jogares:')
for k, v in jogo_ordenado.items():
    pos += 1
    print(f'{pos}º Lugar: {k} com {v}')
    sleep(0.5)