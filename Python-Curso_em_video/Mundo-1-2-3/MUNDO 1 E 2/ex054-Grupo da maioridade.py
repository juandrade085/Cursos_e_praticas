"""Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores. MAIORIDADE 21 ANOS"""
from datetime import date
menor = 0
maior = 0
atual = date.today().year
for pessoa in range (1, 8):
   ano = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
   idade = atual - ano
   if idade < 21:
       menor += 1
   else:
       maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.\n'
      f'E também tivemos {menor} pessoas menores de idade.')
