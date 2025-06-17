"""Faça um programa que peça ao usuário para digitar um número
e, em seguida, exiba todos os múltiplos de 3 até o número fornecido usando
while."""
numero = int(input('Digite um número: '))
multiplos_3 = 0
c = 1
print(f"\033[mOs multiplos de 3 até {numero} são :")
while c <= numero:
    if c % 3 == 0:
        multiplos_3 += 1
        print(c, end=' ')
    c += 1
print(f"\nTotal de múltiplos de 3 encontrados: {multiplos_3}.")

