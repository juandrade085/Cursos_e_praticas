'''Faça um programa que leia um número inteiro e diga se
ele é ou não um número primo.'''

n = int(input('Digite um número: '))
tot = 0
#divisores = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end= '')
        tot += 1
    else:
        print('\033[31m', end= '')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes.')
if tot == 2:
    print(f'E por isso ele É PRIMO.')
else:
    print(f'E por isso ele NÃO É PRIMO.')
