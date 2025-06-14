"""Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços."""
frase = str(input('Digite uma frase: ')).strip().upper()
maiu = frase.replace(" ", '')
invertida = maiu[::-1]#pega do início ao fim de trás pra frente
print (f'O inverso de {maiu} é {invertida}.')
if invertida == maiu:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
