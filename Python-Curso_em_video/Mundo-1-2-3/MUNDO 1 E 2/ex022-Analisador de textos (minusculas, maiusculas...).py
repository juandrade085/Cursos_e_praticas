"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome."""

nome = str(input('Qual seu nome? ')).strip()
print("Analisando seu nome...")
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.strip()) - nome.count(' ')} letras')
div = nome.split()
print(f"Seu primeiro nome é {div[0].capitalize()} e ele tem {len(div[0].strip())} letras")
# ou
print(f'Seu primeiro nome é {div[0].capitalize()} e ele tem {nome.find(' ')} letras.')
