"""Faça um programa que jogue par ou ímpar com o computador.
O jogo será interrompido quando o jogador PERDER, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo."""


from random import randint
v = 0
print('-*=*' * 6)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-*=*' * 6)
while True :
    jogador = int(input('Diga um valor:  '))#Jogador escolhe
    computador = randint(1, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        print(f"{'-' * 24}\n"
              f"Você jogou {jogador} e o computador {computador}. Total de {soma}. ", end= ' '
              f'\nDEU PAR ' if soma % 2 == 0 else 'DEU ÍMPAR '
              f'\n{'=' * 24}')
    if tipo == 'P' :
        if soma % 2 == 0 :
            print('Você VENCEU!')
            v += 1
        else :
            print('Você PERDEU!')
            break
    elif tipo == 'I' :
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
