"""Crie um programa que peça ao usuário uma palavra e
exiba cada letra da palavra em uma linha separada usando um while"""

palavra = str(input('Diga uma palavra: '))
letra = 0
while letra < len(palavra) :
    print(palavra[letra])
    letra += 1