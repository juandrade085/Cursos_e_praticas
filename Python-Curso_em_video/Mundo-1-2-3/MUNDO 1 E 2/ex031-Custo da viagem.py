"""Desenvolva um programa que pergunte a distância de uma viagem
em km. Calcule o preço da passagem, cobranco R$ 0,50 por km para viagem
até 200km e R$ 0,45 para viagens mais longas."""

d = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d:.2f}km.')
"""if d<=200:
    p = d*0.50
else:
    p = d*0.45"""
p = d*0.50 if d<= 200 else d*0.45
print(f'E o preço da sua passagem será de R$ {p:.2f}')
