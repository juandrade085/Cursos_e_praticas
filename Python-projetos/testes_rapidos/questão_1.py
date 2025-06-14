número_par = 0
número_inicial = int(input('Digite um número: '))
while número_par <= número_inicial:
    print(número_par, end='.' if número_par + 1 >= número_inicial else ', ')
    número_par += 2
print('\n---FIM---')