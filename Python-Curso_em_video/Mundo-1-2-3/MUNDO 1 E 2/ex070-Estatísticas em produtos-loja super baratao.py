"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1.000,00.
C) Qual é o produto mais barato."""

soma = maiordemil = quant = barato = 0
produtobarato= ''
print(f'{'-'*40}\n{'LOJA SUPER BARATÃO':^40}\n{'-'*40}')
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    soma += preço
    quant += 1
    if preço > 1000 :
        maiordemil += 1
    if quant == 1 or preço < barato :
        barato = preço
        produtobarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn' :
        break
print(f'{'FIM DO PROGRAMA':=^41}\n'
      f'O total da compra foi R$ {soma:.2f}\n'
      f'Temos {maiordemil} produto(os) custando mais de R$ 1000.00\n'
      f'O produto mais barato foi a/o {produtobarato} que custa R$ {barato:.2f}')
