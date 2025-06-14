"""Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista. """

valores = []
valor_maior = []
valor_menor = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
maior = max(valores)
menor = min(valores)
for pos, valor in enumerate(valores):
    if valor == maior:
       valor_maior.append(pos)
for pos, valor in enumerate(valores):
    if valor == menor:
       valor_menor.append(pos)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições {valor_maior}')
print(f'O menor valor digitado foi {menor} nas posições {valor_menor}')