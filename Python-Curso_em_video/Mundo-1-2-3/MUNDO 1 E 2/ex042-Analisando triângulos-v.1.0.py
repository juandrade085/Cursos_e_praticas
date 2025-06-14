"""Refaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes"""
print(f'{' Analisador de Triângulos ':+^40}')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Os segmentos acima, PODEM FORMAR um triângulo ', end= '')
    if r1 != r2 != r3 != r1 :
        print('ESCALENO.')
    elif r1 == r2 == r3 :
        print('EQUILÁTERO.')
    else :
        print('ISÓSCELES.')
else:
    print('Os segmentos acima, NÃO PODEM FORMAR um triângulo.')
