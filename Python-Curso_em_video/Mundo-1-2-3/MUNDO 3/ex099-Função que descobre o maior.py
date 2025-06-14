"""Faça um programa que tenha uma função chamada maior(), que
receba vários parâmetros com valores inteiros. Seu programa tem que
analisar todos os valores e dizer qual deles é o maior."""

def maior(num):
    print(f"Analisando os valores passados: {num}")
    maior_valor = max(num)
    print(f"O maior valor é {maior_valor}")

valores = []
while True:
    valores.append(int(input('valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
maior(valores)
while True:
    tentar = ' '
    while tentar not in 'SN':
        tentar = str(input('Quer tentar novamente? [S/N] ')).upper().strip()[0]
        if tentar== 'S':
            valores.clear()
            while True:
                valores.append(int(input('valor: ')))
                continuar = ' '
                while continuar not in 'SN':
                    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
                if continuar == 'N':
                    break
            maior(valores)
    if tentar == 'N':
        break
    print('FIM!')
