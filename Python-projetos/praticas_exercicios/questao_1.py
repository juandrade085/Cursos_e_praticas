número_par = 0
número_inicial = int(input('Digite um número: '))
while número_par <= número_inicial:
    if número_par % 2 == 0 :
        print(número_par, end='.' if número_inicial < número_par + 2 else ', ')
    número_par += 2
print('\n--FIM--')