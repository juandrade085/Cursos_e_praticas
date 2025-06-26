"""Peça ao usuário para inserir números inteiros repetidamente. O programa deve calcular a média dos números inseridos
e parar quando o usuário digitar um número negativo."""
soma = 0
contador = 0
while True:
    numero = int(input(f'Digite o {contador + 1}º número (negativo para parar): '))
    if numero < 0:
        break
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f'A média dos números inseridos é {media:.2f}.')
else:
    print('Nenhum número válido foi inserido.')
