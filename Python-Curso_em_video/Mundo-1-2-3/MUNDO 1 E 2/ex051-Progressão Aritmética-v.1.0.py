'''Desenvolva um programa que leia o primeiro termo e
razo de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.'''

print(f'{'=' * 20}\n10 TERMOS DE UMA PA\n{'=' * 20}')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10-1) * razão
for c in range (primeiro, décimo+razão, razão):
    print(c, end= ' → ')
print('ACABOU')