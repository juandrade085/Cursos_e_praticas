"""Implemente um programa que simule um caixa eletrônico. O programa deve pedir um valor inteiro ao usuário
e exibir a quantidade mínima de cédulas (notas de 100, 50, 20, 10, 5, 2 e 1) necessárias para compor o valor."""
from funçoes_questoes.interface import decoração
from funçoes_questoes.numeros import leiaInt
print(f'{decoração(20, '=-')}\n{'BANCO ESTUDOS DA JÚ':^40}\n{decoração(20, '=-')}')

while True:
    valor = leiaInt('Qual valor você quer sacar? R$ ')
    total = valor
    cedulas = [100, 50, 20, 10, 5, 2, 1]

    for cedula in cedulas:
        quantidade = total // cedula
        total %= cedula
        if quantidade > 0 :
            print(f'Total de {quantidade} cédula(s) de R$ {cedula},00')

    continuar = input('Quer sacar mais algum valor? [S/N] ').strip().upper()[0]
    if continuar != 'S':
        break
    else:
        continue

print(f'{'-='*20}\n{'Volte sempre ao BANCO ESTUDOS DA JÚ! Tenha um Bom dia!'}')
