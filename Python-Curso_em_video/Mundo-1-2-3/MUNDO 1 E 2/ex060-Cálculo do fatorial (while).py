"""Faça um programa que leia um número qualquer
e mostre o seu fatorial.
Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
tentar fazer com while e for"""

#com módulo
"""from math import factorial
n = int(input('Digite um número para calcular seu factorial: '))
f = factorial(n)
print(f'O factorial de {n} é {f}.')"""

#modo tradicional
n = int(input('Digite um número para calcular seu factorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0 :
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c # ou f * = c
    c-= 1
print(f'{f}.')


