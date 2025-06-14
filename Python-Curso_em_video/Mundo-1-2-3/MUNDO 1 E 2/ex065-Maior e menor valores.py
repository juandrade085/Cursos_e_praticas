"""Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores."""

resp = 'S' #
média = soma = quant = maior = menor = 0
while resp in 'S' :
    n = int(input("Digite um número inteiro: "))
    soma += n
    média += n
    quant += 1
    if quant == 1 :
        maior = menor = n
    else:
        if n > maior :
            maior = n
        if n < menor :
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} número e a média foi {media}.')
print(f'O maior número digitado foi {maior}.\n'
      f'E o menor foi {menor}.')
print('Fim')
