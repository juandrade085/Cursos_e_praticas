'''co= float(input('Digite o valor do comprimento do cateto opoto: '))
ca= float(input('Digite agora o valor do comprimento do cateto adjacente: '))
h= (co**2+ca**2)**(0.5)
print(f'O valor da hipotenusa desse triângulo é {h:.2f}.')'''

'''co= float(input('Digite o valor do comprimento do cateto opoto: '))
ca= float(input('Digite agora o valor do comprimento do cateto adjacente: '))
h= (co**2+ca**2)**(1/2)
print(f'O valor da hipotenusa desse triângulo é {h:.2f}.')'''


from math import hypot
co= float(input('Digite o valor do comprimento do cateto opoto: '))
ca= float(input('Digite agora o valor do comprimento do cateto adjacente: '))
print(f'O valor da hipotenusa desse triângulo é {hypot(co, ca):.2f}.')