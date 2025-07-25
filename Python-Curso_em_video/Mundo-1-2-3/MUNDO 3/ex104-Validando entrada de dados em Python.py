"""Crie um programa que tenha a função leiaInt(), que vai
funcionar de forma semelhante 'a função input() do Python, só que fazendo a
validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""
def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.strip().isnumeric():
            return int(valor)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
