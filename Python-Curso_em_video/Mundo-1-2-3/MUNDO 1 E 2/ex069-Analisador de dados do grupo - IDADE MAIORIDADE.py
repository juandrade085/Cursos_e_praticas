"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o peograma deverá perguntar se o usuário que ou
não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos."""

totmulher20 = homens = pessoas18 = 0
while True :
    print(f'{'-'*40}\n{'CADASTRE UMA PESSOA':^40}\n{'-'*40}')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18 :
        pessoas18 += 1
    if sexo in 'Mm' :  #B
        homens += 1
    if sexo in 'Ff' and idade < 20 :#C
        totmulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N' :
        break
print(f'{'FIM DO PROGRAMA':=^41}\n'
      f'Total de pessoas com mais de 18 anos : {pessoas18}\n'
      f'Ao todo temos {homens} homens cadastrados.\n'
      f'E temos {totmulher20} mulher(es) com menos de 20 anos.')
