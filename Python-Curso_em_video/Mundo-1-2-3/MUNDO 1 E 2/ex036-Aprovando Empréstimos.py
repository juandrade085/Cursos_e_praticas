"""Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado"""

casa = float(input('Qual valor da casa? R$ '))
salario = float(input('Qual valor do seu salario? R$ '))
tempo = int(input('Quantoss anos de financiamento? '))
finan= casa / (tempo*12)
print (f'Para pagar uma casa de R$ {casa:.2f} em {tempo} anos, ', end='')
print (f'a prestação será de {finan:.2f}')
if finan <= salario * 0.3 :
    print (f'EMPRÉSTIMO APROVADO! PARABÉNS!!!')
else:
    print ('EMPRÉSTIMO NEGADO!')
