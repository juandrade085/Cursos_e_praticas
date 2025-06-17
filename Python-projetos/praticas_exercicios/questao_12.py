"""Escreva um programa que peça ao usuário um número inteiro
positivo, some os dígitos desse número até reduzi-lo a um só dígito
usando while."""

numero = int(input("Digite um número: "))
print(f"{numero} reduzido a um dígito é ", end='')
while numero >= 10:
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    numero = soma
print(f"{numero}.")
