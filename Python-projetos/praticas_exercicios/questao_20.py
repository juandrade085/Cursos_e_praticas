"""Crie um programa que peça ao usuário um número inteiro
positivo e verifique se ele pertence à sequência de Fibonacci."""

print(f"{'→'*30}\n{'SEQUÊNCIA DE FIBONACCI':^30}\n{'←'*30}")
numero = int(input('Digite um número e saiba se ele aparece na sequência: '))

t0, t1 = 0, 1
pertence = False

while t0 <= numero:
    if t0 == numero:
        pertence = True
        break
    t0, t1 = t1, t0 + t1
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
