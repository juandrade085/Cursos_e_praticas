"""Crie um programa que leia vários números inteirOs pelo
teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag)."""

q = s = n = 0 #contar # somar
while n != 999 :
    n = int(input('Digite um valor [999 para parar]: '))
    if n!= 999:
        s += n
        q += 1
print(f'Foram digitados {q} números e a soma entre os eles é {s}.')