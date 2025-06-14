"""Faça um programa que tenha uma função chamada área(), que
receba as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno."""
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.2f} m².')

print(f'{"Controle de Terrenos":^30}\n{"-" * 30}')
largura = float(input(f'Largura (m): '))
comprimento = float(input(f'Comprimento (m): '))
area(largura, comprimento)