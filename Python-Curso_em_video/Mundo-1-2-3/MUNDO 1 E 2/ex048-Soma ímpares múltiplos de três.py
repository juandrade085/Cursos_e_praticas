"""FAça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de três e que se encontram no intervalor de 1
até 500."""
s = 0
n = 0
for c in range(1, 501, 2):
    if c %3 == 0:
        s += c
        n += 1
print(f'O somatório de todos os {n} números ímpares é valores foi {s}.')
