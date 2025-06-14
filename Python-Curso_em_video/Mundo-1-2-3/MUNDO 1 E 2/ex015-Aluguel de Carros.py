d =int(input('Quantos dias alugados? '))
km =float(input('Quantos km rodados? '))
valor =(d*60)+(km*0.15)
#print('O total a pagar é de R$ {:.2f}.'.format(valor))
#ou
print('O total a pagar é de R$ {:.2f}.'.format((d*60)+(km*0.15)))