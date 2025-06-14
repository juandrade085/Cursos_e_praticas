"""Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços."""
frase = str(input('Digite uma frase: ')).strip().upper()
#tirou espaços antes e depois, além de colocar tudo pra maiúscula.
palavras = frase.split() #separou em vetor/lista
junto = ''.join(palavras) #juntou tudo em uma string única
inverso = ''
for letra in range (len(junto) -1, -1, -1):
#foi da última letra, até a primeira, voltando de uma em uma letra
    inverso += junto [letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto :
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')