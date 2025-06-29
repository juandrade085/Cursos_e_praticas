"""Crie um programa que peça números inteiros repetidamente até o usuário digitar "0".
O programa deve contar e exibir quantos desses números possuem soma dos dígitos par. Use um loop while e uma
função auxiliar para calcular a soma dos dígitos."""

from funçoes_questoes.interface import decoração
from funçoes_questoes.numeros import leiaInt, soma_digito

print(f"\033[32m{decoração(35, '←')}\033[m\n{'INFORME NÚMEROS INTEIRO':^35}\n"
      f"{'digite 0 pra parar':^35}\n\033[32m{decoração(35, '←')}\033[m")

valores = []
par = 0

while True:
    numero = leiaInt("Digite um número: ")
    if numero == 0:
        break
    valores.append(numero)
    if soma_digito(numero) % 2 == 0:
        par += 1

print(f"Os números digitos foram: {valores}")
print(f"Desses, {par} têm a soma dos dígitos sendo par.")