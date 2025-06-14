"""Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros"""
print(f'{' LOJAS GUANABARA ':=^40}')
preço = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/PIX\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - ( preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R$ {parcela:.2f} COM JUROS.')
else :
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.')
print(f'Sua compra de R$ {preço:.2f} vai custar R$ {total:.2f} no final.')
