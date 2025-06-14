'''from math import radians, sin, cos, tan
a= float(input('Digite o Ângulo que você deseja: '))
print(f'Dado o ângulo {a}:\nSeno:{sin(radians(a)):.2f}\nCosseno:{cos(radians(a)):.2f}\nTangente: {tan(radians(a)):.2f}.')'''

from math import radians, sin, cos, tan
a= float(input('Digite o Ângulo que você deseja: '))
print('Dado o ângulo {}:\nSeno:{:.2f}\nCosseno:{:.2f}\nTangente: {:.2f}'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
