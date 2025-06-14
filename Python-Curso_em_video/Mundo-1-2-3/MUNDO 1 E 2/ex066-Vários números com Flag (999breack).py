"""Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário, que é a condicão de
parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag)."""

cont = soma = 0
while True :
    numero = int(input('Digite um valor (999 para parar) : '))
    if numero == 999 :
        break
    soma += numero
    cont += 1
print(f'Você digitou {cont} números. A soma entre eles é {soma}.')
