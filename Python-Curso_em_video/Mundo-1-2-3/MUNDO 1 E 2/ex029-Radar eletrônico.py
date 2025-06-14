"""Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite."""

v = float(input('Qual a velocidade atual do carro? '))
if v>80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    print(f'Você deve pagar uma multa de R$ {((v-80)*7):.2f}')
print('Tenha um bom dia. Dirija com segurança!')
