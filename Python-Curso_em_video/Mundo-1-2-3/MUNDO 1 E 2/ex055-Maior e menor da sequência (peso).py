"""Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menos peso lidos."""
menor = maior = 0
for p in range (1, 6):
   peso = float(input(f'Peso da {p}ª pessoa: '))
   if p == 1 :
       menor = peso
       maior = peso
   else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print(f'O maior peso lido foi de {maior:2f}Kg.\n'
      f'O menor peso lido foi de {menor:2f}Kg.')
