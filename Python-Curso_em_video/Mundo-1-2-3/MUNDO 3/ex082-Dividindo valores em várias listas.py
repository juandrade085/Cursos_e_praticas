"""Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
valor = []
valor_par = []
valor_impar= []
while True:
    valor.append(int(input(f'Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
for c in valor :
    if c % 2 == 0:
        valor_par.append(c)
    elif c % 2 == 1:
        valor_impar.append(c)
print(f"{'=-'*20}\nVocê digitou {valor}")
print(f'A lista de pares é {valor_par}')
print(f'A lista de ímpares é {valor_impar}')