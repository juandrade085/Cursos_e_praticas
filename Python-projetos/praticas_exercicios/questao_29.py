"""Escreva um programa que simule o lançamento de um dado (gerar um número entre 1 e 6 aleatoriamente).
O programa deve repetir o lançamento até que saia o número 6 e exibir quantas vezes o dado foi lançado no total."""

from random import randint
from time import sleep
dado = 0
contador = 0

while True:
    contador += 1
    dado = randint(1, 6)
    if dado == 6:
        print("Uhhuuu! Número sorteado: 6\n"
              f"Forma {contador} tentativas!!!")
        break
    else:
        print(f"Número sorteado: {dado}..."
              f"PRÓXIMA RODADA...")
        sleep(2.5)
