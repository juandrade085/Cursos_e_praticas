"""Crie um programa que pergunte ao usuário o valor inicial de
um contador e um valor final. O programa deve contar do valor inicial ao
final, exibindo cada número, usando while."""

valor = int(input('Valor inicial: '))
valor_final = int(input('Valor final: '))
while valor <= valor_final:
    print(f"{valor}", end=' → ' if valor < valor_final else '')
    valor += 1
print(' 🏁')