"""Crie um programa que leia o nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno inidivvidualmente. """
notas_alunos = []
dados_aluno = []

while True:
    dados_aluno.append(str(input('Nome: ')))
    dados_aluno.append(float(input('Nota 1: ')))
    dados_aluno.append(float(input('Nota 2: ')))
    notas_alunos.append(dados_aluno[:])
    dados_aluno.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f"{'=-' * 25}")
print(f'{'-' * 30}\n{"Nº":<5}{"NOME":<10}{"MÉDIA":>5}\n{'-' * 30}')
for num, aluno in enumerate(notas_alunos):
    if aluno in notas_alunos :
        print(f'{num+1:<5}', end='')
        print(f'{aluno[0]:<10}', end='')
        media = (aluno[1]+aluno[2])/2
        print(f'{media:>5.1f}')
print(f'{'-' * 30}')
while True:
    detalhes = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if detalhes != 999:
        print(f'Notas de {notas_alunos[detalhes-1][0]} são [{notas_alunos[detalhes-1][1]},{notas_alunos[detalhes-1][2]}]')
    else:
        print('VOLTE SEMPRE')
        break
print(f'{'-' * 30}')
