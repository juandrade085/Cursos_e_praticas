"""Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valor 'M' e 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto."""

"""s = 1
while s != 'F' and s != 'M':
    s = str(input('Qual seu sexo? [F/M] ')).upper().strip()[0]
    if s != 'F' and s != 'M' :
        print(f'Dados inválidos!')
print(f'Sexo {s} registrado com sucesso.')"""


sexo = str(input('Qual seu sexo? [F/M] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso.')