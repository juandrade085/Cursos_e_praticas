"""Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares"""
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou {num}')
v = 0

# a) Quantas vezes apareceu o valor 9
print(f'Você digitou os valores {num}\n'
      f'O valor 9 apareceu {num.count(9)} vezes.'
      if 9 in num else 'Não teve nenhum número 9.')

# b) Em que posição foi digitado o primeiro valor 3
print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.'
      if 3 in num else 'Não teve nenhum número 3.')

# c) Quais foram os números pares
print('Números pares digitados: ', end=' ')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
        v += 1
if v == 0:
    print('Não teve número par.')
else:
    print(f'\nVocê Digitou {v} números pares.')
