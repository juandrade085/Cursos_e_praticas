"""Crie um programa que mostre na tela todos os números pares que
estão no intervalo entre 1 e 50."""

'''pode ser:'''

print('Esses são os números pares entre 1 e 50:')
for c in range (1, 50):
    if c % 2== 0:
        print(c, end=' ')
print('Acabou')

'''print('Esses são os números pares entre 1 e 50:')
for c in range (2, 51, 2):
    print(c, end=' ')'''
