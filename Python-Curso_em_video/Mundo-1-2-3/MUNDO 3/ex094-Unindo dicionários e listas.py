"""Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
dados = []
pessoas = {}
soma_idade = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).title()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Opção inválida. Digite apenas M ou F:')
    pessoas['idade'] = int(input('Idade: '))
    soma_idade += pessoas['idade']
    dados.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Opção inválida. Digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 20)
print(dados)
print('-=' * 20)
#A) Quantas pessoas foram cadastradas
print(f'A) - O grupo tem {len(dados)} pessoas.')

#B) A média de idade
media = soma_idade / len(dados)
print(f'B) - A média de idade é de {media:.2f} anos.')

#C) Uma lista com as mulheres
print(f'C) - As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
#D) Uma lista de pessoas com idade acima da média
print(f'\nD) - Lista das pessoas que estão acima da média de idade:\n')
for p in dados:
    if p['idade'] >= media :
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print(f'>>ENCERRADO<<')