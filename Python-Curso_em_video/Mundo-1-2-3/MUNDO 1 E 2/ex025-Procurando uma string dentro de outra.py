# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome
n = input('Qual é seu nome completo? ').strip()
print(f'Seu nome tem Silva?', "SILVA" in n.upper())
