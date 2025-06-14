"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de
uma PA, mostrando os 10 primeiros termos da progressão usando a
estrutura while."""


"""print(f'{'=' * 20}\n10 TERMOS DE UMA PA\n{'=' * 20}')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + ((10-1) * razao)
c = primeiro
while c < (decimo+razao):
    print(c, end=' → ')
    c +=razao
print('ACABOU')"""

print(f'{'=' * 20}\nGERADOR DE PA\n{'=' * 20}')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' → ')
    termo +=razao
    cont += 1
print('ACABOU')
