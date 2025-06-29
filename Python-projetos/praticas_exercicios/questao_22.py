"""Faça um programa que peça números inteiros ao usuário usando um loop while. O programa deve continuar
pedindo números enquanto a soma acumulada for menor que 200. Quando a soma ultrapassar 200, exiba quantos números
foram digitados."""
soma = contador = 0
numeros = []
while soma < 200 :
    numero = int(input("Digite um número para a soma: "))
    numeros.append(numero)
    soma += numero
    contador += 1
print(f"Com {contador} números digitados, somou {soma}.")
print(numeros)
