"""Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte aousuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor
seão entregues.
OBS.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1."""
print(f'{'=-'*20}\n{'BANCO CEV':^40}\n{'-='*20}')
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced :
        total -= ced
        totced += 1
    else:
        if totced > 0 :
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 100 :
            ced = 50
        elif ced == 50 :
            ced = 20
        elif ced == 20 :
            ced = 10
        elif ced ==  10 :
            ced = 1
        totced = 0
        if total == 0 :
            break
print(f'{'-='*20}\n{'Volte sempre ao BANCO CEV! Tenha um Bom dia!'}')
