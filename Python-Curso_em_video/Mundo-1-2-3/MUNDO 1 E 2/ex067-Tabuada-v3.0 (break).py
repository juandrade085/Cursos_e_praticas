"""Faça um programa que mostre a tabuada de vários números, um
de cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
"""

while True :
    n = int(input(f"{'-' * 33}\nQuer ver a tabuada de qual valor? "))
    print(f'{'-' * 33}')
    for c in range (0, 11) :
        print(f'{n} x {c} = {n*c}')
    if n > 0:
        break
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE')
