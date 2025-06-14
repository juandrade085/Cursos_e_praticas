"""Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente. """
valores = []
while True:
    valor = (int(input(f'Digite um valor: ')))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar na lista.')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f"{'=-'*20}\nVocê digitou os valores {sorted(valores)}")
