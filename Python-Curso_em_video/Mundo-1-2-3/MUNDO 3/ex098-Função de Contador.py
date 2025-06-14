"""Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo. Seu programa tem que
realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep

def contador(a, b, c):
    if c == 0:
        print("ERRO! Passo 0 é inválido! Considerando passo 1.")
        c = 1
    if a > b and c > 0:
        c = -c
    if a < b and c < 0:
        c = -c

    passo_mostrar = c if c > 0 else -c
    print(f"{'~=' * 20}\nContagem de {a} até {b} de {passo_mostrar} em {passo_mostrar}")

    for n in range (a, b + (1 if c > 0 else -1), c):
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print(f"{'~=' * 20}\nAgora é sua vez de personalizar a contagem!")
num1, num2, num3 = int(input("Início: ")), int(input("Fim: ")), int(input("Passo: "))
contador(num1, num2, num3)