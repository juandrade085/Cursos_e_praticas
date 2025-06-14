"""Crie um programa que leia um número inteiro e mostre na
tela se ele é par ou ímpar."""

n = int(input('Me diga um número qualquer: '))
r = n%2
if r==0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é ÍMPAR')