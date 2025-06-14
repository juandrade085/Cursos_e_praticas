"""Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais."""

palavras = ('fotografa', 'chef', 'modelo', 'bailarina', 'animador',
            'marinheiro', 'optometrista', 'nutricionista', 'medico',
            'veterinaria', 'verde', 'vermelho', 'prateado', 'amarelo',
            'azul', 'laranja', 'preto', 'marrom', 'cinza', 'vermelho')
vogais = "aeiou"
for palavras in palavras:
    print(f'\nNa palavras {palavras.upper()} temos ', end='')
    for letras in vogais:
        if letras.lower() in palavras:
            print(letras, end=' ')
print('\n-FIM-')
