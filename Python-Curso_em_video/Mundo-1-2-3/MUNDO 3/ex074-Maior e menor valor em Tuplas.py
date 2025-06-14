"""Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de números
gerados e também indique o menor e o maior valor que estão na tupla."""

#do professor
"""from random import randint
num = (randint(0, 100), randint(0, 100), randint(0, 100),
     randint(0, 100), randint(0, 100))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')"""

from random import randint
n = (randint(0, 100), randint(0, 100), randint(0, 100),
     randint(0, 100), randint(0, 100))
print(f'Os valores sorteados foram {n}')
menor = maior = sorted(n)
print(f'O menor número é {menor[0]} e o maior é {maior[-1]}')

