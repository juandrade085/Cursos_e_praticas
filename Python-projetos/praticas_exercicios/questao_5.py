"""Faça um programa que peça ao usuário um número e,
em seguida, exiba a tabuada desse número de 1 a 10 usando while."""

while True :
    numero = int(input(f"Quer ver a tabuada de qual número? "))
    print(f"{'~'*20}\n{'TABUADA DE':>12} {numero:<6}\n{'~'*20}")
    for c in range (0, 11) :
        largura = len(str(numero))+2
        print(f'{numero:>{largura}} x {c:>2} = {numero*c:>{largura}}')
    if numero > 0:
        break

print(f'TABUADA 0 a 10 do número {numero} finalizada.\nVOLTE SEMPRE')
