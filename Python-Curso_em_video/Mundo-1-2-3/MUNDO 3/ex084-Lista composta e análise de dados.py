"""Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves."""
pessoas = []
peso = []
maiorpeso = menorpeso = 0
while True:
    peso.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = peso[1]
    else:
        if peso[1] > maiorpeso:
            maiorpeso = peso[1]
        if peso[1] < menorpeso:
            menorpeso = peso[1]
    pessoas.append(peso[:])
    peso.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
#a) Quantas pessoas foram cadastradas;
print(f"{'=-'*20}\nTemos {len(pessoas)} cadastradas.")

#b) Uma listagem com as pessoas mais pesadas;
print(f"O maior peso foi de {maiorpeso}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == maiorpeso :
        print(f"[{p[0]}] ", end='')
print()

#c) Uma listagem com as pessoas mais leves.
print(f"O maior peso foi de {menorpeso}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == menorpeso :
        print(f"[{p[0]}] ", end='')
print()
