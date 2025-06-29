"""Faça um programa que peça ao usuário para digitar dois números. O programa deve calcular o máximo
divisor comum (MDC) desses dois números usando o algoritmo de Euclides com while."""

numero_1 = int(input('Primeiro número: '))
numero_2 = int(input('Segundo número: '))

# verificando quem é menor e maior
while numero_2 != 0:
    numero_1, numero_2 = numero_2, numero_1 % numero_2
print("MDC:", numero_1)

