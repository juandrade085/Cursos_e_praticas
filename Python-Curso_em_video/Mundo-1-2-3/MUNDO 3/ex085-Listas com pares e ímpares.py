"""Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separadosos valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente."""

par_impar  = [[], []]
num = 0
for c in range (1, 8):
    num = (int(input(f'Digite o {c}º valor: ')))
    if num % 2 == 0:
        par_impar[0].append(num)
    else:
        par_impar[1].append(num)
par_impar[0].sort()
par_impar[1].sort()
print(f"{'=-'*20}\nOs valores pares digitados foram: {par_impar[0]}\n"
      f"Os valores ímpares digitados foram: {par_impar[1]}")


