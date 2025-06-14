"""Faça um programa que ajude um jogador da MEGA SENA a criar
palpites.O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
lista composta."""
from random import randint
from time import sleep
lista_apostas = []

print(f"{'-' * 42}\n{'JOGO NA MEGA SENA':^40}\n{'-' * 42}")
jogos= int(input(f'Quantos jogos você quer que eu sorteie? '))
print(f"{'=-'*6} SORTEANDO {jogos} jogos {'=-'*6}")
for n in range (0, jogos):
    aposta = []
    while len(aposta) < 6:
        numero = randint(1, 60)
        if numero not in aposta:
            aposta.append(numero)
        else:
            numero = randint(1, 60)
    aposta.sort()
    lista_apostas.append(aposta)
for pos, jogo in enumerate(lista_apostas):
    print(f"Jogo {pos+1}: {jogo}")
    sleep(1)
print(f"{'=-' * 7} < BOA SORTE > {'=-' * 7}")
