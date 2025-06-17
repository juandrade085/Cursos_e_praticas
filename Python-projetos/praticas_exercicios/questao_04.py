"""Peça ao usuário para digitar números inteiros
repetidamente até que ele digite "0". No final, exiba a soma de todos
os números digitados."""

soma_total = contador_numeros = 0
while True:
    numero = int(input('Digite um número inteiro (0 para parar): '))
    if numero == 0:
        break
    soma_total += numero
    contador_numeros += 1

print(f'\nO somatório de todos os {contador_numeros} números foi {soma_total}.')
