"""Escreva um programa que calcule o produto de todos os números inteiros de 1 até um número fornecido pelo
usuário usando while."""

print(f"{'→'*35}\n{'✎𓂃MÁQUINA DE PRODUTO🔢':^30}\n{'←'*35}")
numero_limite = int(input("Digite o número máximo: "))
c = c1 = 1
while c<= numero_limite:
    print(c, end=' x ' if c < numero_limite else ' = ')
    c1 *= c
    c += 1
print(c1)
