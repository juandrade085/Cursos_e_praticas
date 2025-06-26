"""Crie um programa que conte de 1 até 100 e exiba somente os números divisíveis por 5 usando while."""

c = 5
print("Os divisíveis por 5 até 100 são :")
while c <= 100:
    print(f"\033[36m{c}\033[m", end='.' if c == 100 else ', ')
    c += 5
print()