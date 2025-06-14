"""Crie um programa que tenha uma tupla única com nomes de
produtos e seus respectivos preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular."""
lista = ('Achocolatado', 5.8,
         'Açúcar refinado', 2.29,
         'Água mineral sem gás', 2.9,
         'Água sanitária', 2.99,
         'Alface', 1.99,
         'Arroz', 5.59,
         'Banana', 2.99,
         'Batata', 2.99,
         'Café', 10.98,
         'Carne de Frango', 5.99,
         'Carne moída de gado', 25.9,
         'Carne Paleta de gado', 14.9,
         'Carne suína pernil', 10.98,
         'Cebola', 4.9,
         'Cenoura', 4.8,
         'Detergente', 1.79,
         'Feijão', 5.99)

print(f'{'-' * 45}\n{"LISTAGEM DE PREÇOS":^40}\n{'-' * 45}')
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<35}', end='')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
print('-' * 45)