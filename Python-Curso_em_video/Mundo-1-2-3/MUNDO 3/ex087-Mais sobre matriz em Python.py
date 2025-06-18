"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares  = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

#formato da matriz
print(f"{'=-' * 20}")
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

# A) A soma de todos os valores pares digitados.
    if matriz[linha][coluna] % 2 == 0:
        soma_pares += matriz[linha][coluna]
    print()
print(f"A soma dos valores pares é {soma_pares}")

#B) A soma dos valores da terceira coluna.
soma_3ºcoluna = 0
for linha in matriz:
    soma_3ºcoluna += linha[2]
print(f"A soma dos valores da terceira coluna é {soma_3ºcoluna}")

#C) O maior valor da segunda linha.
maior = matriz[1][0]
for n in matriz[1]:
    if n > maior :
        maior = n
print(f'O maior valor da segunda linha é {maior}.')
