"""Crie um programa que leia dois valores e mostre um
menus na tela:
[1] somar
[2] multiplicar
[3] maior #saber qual é o maior valor
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

soma = 1
multiplicar = 1
opção = 0
v1 = int(input('Digite um número inteiro: '))
v2 = int(input('Digite outro número inteiro: '))
while opção!= 5:
    print('***MENU***\n'
          '[ 1 ] SOMAR\n'
          '[ 2 ] MULTIPLICAR\n'
          '[ 3 ] NÚMERO MAIOR\n'
          '[ 4 ] NOVOS NÚMEROS\n'
          '[ 5 ] SAIR DO PROGRAMA\n')
    opção = int(input('Qual é a opção? '))
    if opção == 1 :
        print(f'A Soma entre {v1} e {v2} é igual a {v1+v2}.')
    elif opção == 2 :
        print(f'A Multiplicação entre {v1} e {v2} é igual a {v1*v2}.')
    elif opção == 3 :
        if v1 > v2 :
            maior = v1
        else :
            maior = v2
        print(f'O número maior é {maior}.')
    elif opção == 4 :
        v1 = int(input('Digite um número inteiro: '))
        v2 = int(input('Digite outro número inteiro: '))
    elif opção == 5 :
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa! Volte sempre.')

