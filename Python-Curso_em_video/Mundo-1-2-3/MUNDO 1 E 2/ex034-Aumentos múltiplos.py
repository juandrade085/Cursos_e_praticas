'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule
um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

s = float(input('Qual seu salário atual? R$ '))
if s > 1250:
    a = (s * 0.10) + s
else:
    a = (s * 0.15) + s
'''if s <= 1250:
    a = s + (s * 15 / 100)
else:
    a = s + (s * 10 / 100)'''
print(f'Seu novo salário será R$ {a:.2f}')