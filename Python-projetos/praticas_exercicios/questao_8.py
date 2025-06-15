"""Implemente um programa que leia um número inteiro
positivo e mostre os seus divisores usando while."""

numero = int(input("Digite um número: "))
divisores = 1
print(f"Divisores de {numero}")
while divisores <= numero:
    if numero % divisores == 0:
        print(divisores, end=' ')
    divisores += 1
