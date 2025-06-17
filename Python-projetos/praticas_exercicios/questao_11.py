"""Crie um programa que peça um número inteiro ao usuário
e determine se ele é primo. Use o loop while para verificar os divisores
do número."""
numero = int(input('Digite um número: '))
total_divisores = 0
c = 1
while c <= numero+1 :
    if numero % c == 0:
        print('\033[34m', end='')
        total_divisores += 1
    else:
        print('\033[31m', end='')
    print(f"{c} ", end='\n' if c % 15 == 0 else ' ')
    c += 1
print(f"\n\033[mO número {numero} foi divisível {total_divisores} vezes.")
if total_divisores == 2:
    print(f"E por isso ele É PRIMO.")
else:
    print(f"E por isso ele NÃO É PRIMO.")