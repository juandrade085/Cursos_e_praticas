"""Crie um programa que peça ao usuário números inteiros. O programa deve continuar pedindo
enquanto o número digitado for diferente de zero. Ao final, exiba:
Quantos números foram digitados (sem contar o zero), a média desses números, e o maior valor informado."""

from funçoes_questoes.numeros import leiaInt
from funçoes_questoes.interface import decoração

print(f"\033[32m{decoração(35, '←')}\033[m\n{'INFORME NÚMEROS INTEIRO':^35}\n"
      f"{'digite 0 pra parar':^35}\n\033[32m{decoração(35, '←')}\033[m")

numero = []
soma = 0

while True:
    valor = leiaInt("Digite números inteiros: ")
    if valor == 0:
        break
    soma += valor
    numero.append(valor)
if len(numero) > 0 :
   media = soma/len(numero)
   print(f'Você digitou {len(numero)} números.'
         f'A média dos números foi de {media}.')
