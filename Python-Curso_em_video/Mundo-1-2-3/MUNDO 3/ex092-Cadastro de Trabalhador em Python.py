"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import date
funcionario = dict()
atual = date.today().year
funcionario['nome'] = str(input('Nome: ')).title()
nascimento = int(input(f'Ano de Nascimento: '))
funcionario['idade'] = atual - nascimento
funcionario['ctps'] = int(input(f'Carteira de Trabalho (0 não tem): '))
if funcionario['ctps'] != 0 :
    funcionario['contratação'] = int(input(f'Ano de contratação: '))
    funcionario['salário']= float(input(f'Salário: R$ '))
    funcionario['aposentaria'] = funcionario['contratação']+35-nascimento
print('-='*15)
print(funcionario)
for k, v in funcionario.items():
   print(f' - {k} tem o valor {v}')