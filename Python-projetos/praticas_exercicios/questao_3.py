"""Implemente um programa que peça um número inteiro
positivo ao usuário e exiba a soma dos números ímpares de 1 até esse
número usando o loop while."""

soma = 0
numeros_impares = 0
c = 1
numero_limite = int(input('Digite um número inteiro : '))
while c <= numero_limite :
    if c % 2 == 1:
        soma += c
        numeros_impares += 1
        print(c, end=' ')
    c += 1
print(f'\nO somatório de todos os {numeros_impares} números ímpares foi {soma}.')
