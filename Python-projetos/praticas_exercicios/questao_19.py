"""Escreva um programa que conte quantos números entre 1 e 1000 são divisíveis por 7 usando while."""

c = 1
contador = 0
organizador = 0

while c <= 1000:
    if c % 7 == 0:
        print(f"{c:4} ", end='')
        organizador += 1
        if organizador == 10:
            print()
            organizador = 0
        contador += 1
    c += 1
print()
print(f"\nTotal de números divisíveis por 7 entre 1 e 1000: {contador}")
