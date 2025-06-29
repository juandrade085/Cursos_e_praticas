"""Escreva um programa que peça ao usuário para digitar um número inteiro positivo n. O programa deve usar um
loop while para imprimir todos os números de 1 até n que não são divisíveis por 3 nem por 5."""

n = int(input("Digite um número inteiro: "))
print(f'Os números NÃO divisíveis por 3 ou 5 de 0 a {n} são:')
c = 1
organizador = 0
while c <= n:
    if c % 3 > 0 and c % 5 > 0 :
        print(f"{c:4}", end='')
        organizador += 1
        if organizador == 13:
            print()
            organizador = 0
    c += 1
print()