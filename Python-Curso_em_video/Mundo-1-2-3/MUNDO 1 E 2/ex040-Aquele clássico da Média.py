"""Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO"""
print(10 * ' = x' + ' =')
print(f'{'Calcule sua nota':^38}')
print(10 * ' = x' + ' =')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Com a nota {n1:.1f} e {n2:.1f}, você atingiu a nota {media:.1f}.')
if media < 5 :
    print('Mas, infelizmente, com essa nota, você está REPROVADO.')
elif 7 > media >= 5 :
    print('Mas, infelizmente, com essa nota, você está em RECUPERAÇÃO.')
else :
    print('PARABÉNS! Com essa nota, você foi APROVADO!')
