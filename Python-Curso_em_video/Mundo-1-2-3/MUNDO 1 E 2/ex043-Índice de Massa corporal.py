"""Desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida"""
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC  dessa pessoa é de {imc:.1f}.')
if imc < 18.5 :
    print('ATENÇÃO, você está abaixo do Peso.')
elif 18.5 <= imc < 25 :
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30 :
    print('ATENÇÃO, você está em SOBREPESO.')
elif 30 <= imc < 40 :
    print('ATENÇÃO, você está em OBESIDADE.')
elif imc >= 40 :
    print('ATENÇÃO, você está em OBESIDADE MÓRBIDA.')
