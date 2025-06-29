"""Crie um programa que peça ao usuário uma sequência de números e exiba o maior número inserido.
O programa deve encerrar quando o usuário digitar "sair"."""
from funçoes_questoes.interface import decoração

print(f"\033[32m{decoração(35, '←')}\033[m\n{'INFORME NÚMEROS INTEIRO':^35}\n"
      f"{'digite SAIR pra parar':^35}\n\033[32m{decoração(35, '←')}\033[m")
valores = []
while True:
    entrada = input('NÚMERO:').upper().strip()
    if entrada.isdigit():
        numero = int(entrada)
        valores.append(numero)
        continue
    if entrada == 'SAIR':
        break
    print("Nenhum número foi digitado, TENTE NOVAMENTE." if not valores else
          "Entrada inválida. Digite um número inteiro ou 'SAIR' para encerrar.")
if valores:
    print(f"O maior número inserido foi {max(valores)}")
else:
    print("Você saiu sem digitar nenhum número.")
