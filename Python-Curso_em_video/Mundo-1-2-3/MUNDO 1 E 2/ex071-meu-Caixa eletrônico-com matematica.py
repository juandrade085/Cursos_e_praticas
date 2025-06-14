"""Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte aousuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor
seão entregues.
OBS.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1."""





print(f'{'=-'*20}\n{'BANCO CEV':^40}\n{'-='*20}')
valor = cinquenta = vinte = dez = um = 0
while True:
    valor = int(input('Qual valor você quer sacar? R$ '))
    cinquenta = valor // 50
    vinte = (valor % 50)//20
    dez = ((valor % 50)%20)//10
    um = (((valor % 50)%20)%10)//1
    print(f'Total de {cinquenta} cédulas de R$ 50,00\n'
          f'Total de {vinte} cédulas de R$ 20,00\n'
          f'Total de {dez} cédulas de R$ 10,00\n'
          f'Total de {um} cédulas de R$ 1,00\n')
    continuar = ' '
    while continuar in 'SN' :
        continuar = str(input('Quer sacar mais algum valor? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn' :
        break
print(f'{'-='*20}\n{'Volte sempre ao BANCO CEV! Tenha um Bom dia!'}')
