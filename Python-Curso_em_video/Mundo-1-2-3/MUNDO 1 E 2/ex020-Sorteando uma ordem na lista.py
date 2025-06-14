'''from random import sample
a= input('Digite o nome dos alunos que participarão da apresentação: ')
b= input('Digite o nome dos alunos que participarão da apresentação: ')
c= input('Digite o nome dos alunos que participarão da apresentação: ')
aluno= sample([a, b, c], k=3)
print(f'A ordem da apresentação será a seguinte: {aluno}')'''

from random import shuffle
a= input('Digite o nome dos alunos que participarão da apresentação: ')
b= input('Digite o nome dos alunos que participarão da apresentação: ')
c= input('Digite o nome dos alunos que participarão da apresentação: ')
d= input('Digite o nome dos alunos que participarão da apresentação: ')

lista= [a, b, c, d]
shuffle(lista)
print(f'A ordem da apresentação será a seguinte: {lista}')