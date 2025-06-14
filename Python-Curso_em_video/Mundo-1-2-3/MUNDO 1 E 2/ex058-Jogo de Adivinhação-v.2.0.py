from random import randint
computador = randint(0, 10)
print('-*=*' * 13)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-*=*' * 13)
acertou = False
palpite = 0
jogador = 1
computador = 0
while not acertou :
    jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar
    palpite += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador :
            print('Mais... Tente mais uma vez.')
        elif jogador > computador :
            print('Menos... Tente mais uma vez.')
print(f'Você precisou de {palpite} tentativas pra vencer!!!')
print('Parabéns! Você conseguiu me vencer!!!')
