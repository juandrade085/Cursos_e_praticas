'''Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o.'''

s = 0 #somar
cont = 0 #contar
for c in range (1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'O somatório de todos os {cont} números pares foi {s}.')
