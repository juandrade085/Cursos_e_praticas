"""MEU DESAFIO-Crie um programa que pergunte uma frase, crie
tupla com as palavras dessa frase, (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais."""

frase = (str(input('Digite uma frase: \n')))
vogais = "aeiou"
letras = ''
div = frase.split()
for frase in div:
    print(f'\nNa palavra {frase.upper()} temos ')
    for letras in vogais:
        if letras.lower() in frase:
            print(letras, end=' ')
    if letras not in frase:
        print('zero vogais.', end='')
print('\n-FIM-')
