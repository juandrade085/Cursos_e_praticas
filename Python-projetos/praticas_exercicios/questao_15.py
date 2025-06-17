"""Implemente um programa que calcule a sequência de Fibonacci
até o número n fornecido pelo usuário usando o loop while."""

print(f"{'→'*30}\n{'SEQUÊNCIA DE FIBONACCI':^30}\n{'←'*30}")
n = int(input('Digite um número: '))

termo_1, termo_2 = 0, 1
print(f'{termo_1}', end='')

while termo_2 <= n:
    print(f' → {termo_2}', end='')
    termo_1, termo_2 = termo_2, termo_1 + termo_2

print(' → FIM')

