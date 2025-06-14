'''Refaça o desafio 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando o laço for.'''

n = int(input('Digite um número para ver sua tabuada: '))
print(f'{'-' * 14}')
for c in range (0, 11):
    print(f'{n} x {c} = {n*c}')
print(f'{'-' * 14}')
