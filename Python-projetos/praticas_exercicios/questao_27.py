"""Faça um programa que peça ao usuário para inserir números inteiros repetidamente e exiba quantos números
pares e ímpares foram inseridos. O programa deve parar quando o usuário digitar "-1"."""

from funçoes_questoes.interface import decoração
from funçoes_questoes.numeros import leiaInt

print(f"\033[32m{decoração(35, '←')}\033[m\n{'INFORME NÚMEROS INTEIRO':^35}\n"
      f"{'digite -1 pra parar':^35}\n\033[32m{decoração(35, '←')}\033[m")
numero_pares = []
numero_ímpares = []

while True:
    valor = leiaInt("Número: ")
    if valor == -1:
        break
    else:
        if valor % 2 == 0:
            numero_pares.append(valor)
        else:
            numero_ímpares.append(valor)

print(f"\n\033[36m=== RESULTADO FINAL ===\033[m"
      f"\n\033[34mOs números pares digitados foram {sorted(numero_pares)}\033[m"
      f"\n\033[35mE os números ímpares digitados foram {sorted(numero_ímpares)}\033[m")