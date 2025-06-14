"""Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista. """

valores = []
valor_maior = 0
valor_menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0 :
        valor_maior = valor_menor = valores[cont]
    else:
        if valores[cont] > valor_maior:
            valor_maior = valores[cont]
        if valores[cont] < valor_menor:
            valor_menor = valores[cont]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {valor_maior} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == valor_maior:
       print(f'{pos}...', end='')
print(f'\nO menor valor digitado foi {valor_menor} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == valor_menor:
       print(f'{pos}...', end='')
