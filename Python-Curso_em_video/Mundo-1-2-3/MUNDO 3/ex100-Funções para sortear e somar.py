"""Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função vai sortear
5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
from time import sleep


def sorteia(lista):
    print(f"{'=-' * 20}\nSorteando 5 valores:", end=' ')
    for n in range(5):
        numeros = randint(1, 10)
        lista.append(numeros)
        print(f'{numeros} ', end='')
        sleep(0.3)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} temos {soma}')
    print('Pronto!')

valores = []
sorteia(valores)
somaPar(valores)
