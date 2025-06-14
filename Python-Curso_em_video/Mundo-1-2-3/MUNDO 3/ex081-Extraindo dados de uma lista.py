"""Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
valor = []
while True:
    valor.append(int(input(f'Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f"{'=-'*20}\nVocê digitou {len(valor)} elementos.")
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')
print(f'O valor 5 faz parte da lista!'
      if 5 in valor else 'O valor 5 não faz parte da lista!')