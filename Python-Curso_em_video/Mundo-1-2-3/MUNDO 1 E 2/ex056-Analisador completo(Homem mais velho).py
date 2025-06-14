"""Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos"""
soma = 0
part = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
   print(f"{'-' * 10}{p}ª PESSOA{'-' * 10}")
   nome = str(input(f'Nome: ')).strip()
   idade = int(input(f'Idade: '))
   sexo = str(input(f'Sexo [M/F]: ')).upper().strip()
   part += 1
   soma += idade
   if p == 1 and sexo in 'Mm':
      maioridadehomem = idade
      nomevelho = nome
   if sexo in 'Mm' and idade > maioridadehomem:
      maioridadehomem = idade
      nomevelho = nome
   if sexo in 'Ff'and idade < 20:
      totmulher20 += 1
media = soma / part
print(f"A média de idade do grupo é de {media:.2f} anos.\n"
      f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.\n'
      f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
