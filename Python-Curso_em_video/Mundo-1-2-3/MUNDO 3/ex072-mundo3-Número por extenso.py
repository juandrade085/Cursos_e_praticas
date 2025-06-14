"""Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. Pergunte se quer
continuar ou não."""
n = ('zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
while True:
    a = int(input('Digite um número entre 0 e 20: '))
    if a < 0 or a > 20:
        a = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {n[a]}.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{'FIM DO PROGRAMA':=^41}\n')

