
"""Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo."""

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    resposta = 'possível'
else:
    resposta = 'impossível'
print(f'Com essas medidas é {resposta} formar um triângulo.')
