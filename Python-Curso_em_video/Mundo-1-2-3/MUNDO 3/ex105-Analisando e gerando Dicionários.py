"""Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornar um dicionário com as
seguintes informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo
desenvolvedor."""

def notas(*num, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações da turma.
    """
    boletim = dict()
    boletim['total'] = len(num)
    boletim['maior'] = max(num)
    boletim['menor'] = min(num)
    boletim['media'] = round(sum(num) / len (num), 2)
    if sit :
        if boletim['media'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['media'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim

# Programa Principal
resp = notas (5.5, 8.5, 9, 10, 2.5, sit=True)
print(resp)
#help(notas)
