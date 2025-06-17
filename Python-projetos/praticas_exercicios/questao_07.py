"""Escreva um programa que calcule o fatorial de um número
digitado pelo usuário usando o loop while."""

# Tradional
numero_fatorial = int(input('Digite um número para calcular seu factorial: '))
inteiros_menores = numero_fatorial
produto = 1

print(f"Calculando {numero_fatorial}! = ", end='')
while inteiros_menores > 0 :
    print(f"{inteiros_menores}", end=' x ' if inteiros_menores > 1 else ' = ')
    produto *= inteiros_menores
    inteiros_menores-= 1
print(f'{produto}.')
