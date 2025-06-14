"""Faça um program que leia o sexo e o ano de nascimento de um
jovem, informe se ele precisa se alistar. Caso sim, de acordo com a sua
idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
print('''Qual seu sexo:
[ 1 ] FEMININO
[ 2 ] MASCULINO''')
opção = int(input('Sua opção : '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if opção == 1:
    print('Mas seu alistamento não é obrigatório. Tenha um bom dia.')
elif opção == 2 and idade < 18:
    print(f'Ainda faltam {18-idade} anos para o alistamento.\n'
          f'Seu alistamento será em {atual+(18-idade)}.')
elif opção == 2 and idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18}.\n'
          f'Seu alistamento foi ou deveria ter sido em {atual-(idade-18)}.')
elif opção == 2 and idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else :
    print(f'Opção inválida. Tenha um bom dia.')
