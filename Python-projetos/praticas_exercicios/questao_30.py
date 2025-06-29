#⭐ FAVORITO por ter sido de um domingo de sol ☀️
"""Escreva um programa que peça ao usuário para digitar números inteiros positivos um por vez, usando um loop while.
O programa deve continuar pedindo números até que o usuário digite um número maior que 100.
Durante a entrada, o programa deve imprimir apenas os números que são múltiplos de 4.
No final, o programa deve exibir a quantidade total de números múltiplos de 4 digitados."""

from funçoes_questoes.interface import decoração, tempo
from funçoes_questoes.numeros import leiaInt

numero = []

print(f"\033[32m{decoração(35, '←')}\033[m"
      f"\n{'INFORME NÚMEROS INTEIRO':^35}\n"
      f"{'digite um número > 100 pra parar':^35}\n"
      f"\033[32m{decoração(35, '←')}\033[m")

while True:
    valor = leiaInt("Digite um número: ")
    if valor > 100:
        print(">>> PROGRAMA FINALIZADO <<<\n"
              f"Foram {len(numero)} múltiplos de 4 validados.")
        break
    if valor > 0:
        if valor % 4 == 0:
            numero.append(valor)
            print(f"{valor} é multiplo de 4."
                  f"...salvando", end='')
            tempo(0.5, '.',3)
        else:
            print(f"{valor} não é múltiplo de 4.")
    else:
        print('Zero é um número inválido...')
    print(f"\n{numero}")
