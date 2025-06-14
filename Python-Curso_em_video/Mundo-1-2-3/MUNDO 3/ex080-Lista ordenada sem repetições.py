"""Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista, já na posição correta de
inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""
valores = []
for c in range(0, 5):
    numeros = int(input(f'Digite um valor: '))
    if c == 0 or numeros > valores [-1]:
        valores.append(numeros)
        print(f'Adicionando o valor ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if numeros <= valores[posicao]:
                valores.insert(posicao, numeros)
                print(f'Adicionando valor a posição {posicao} da lista.')
                break
            posicao += 1
print(f"{'=-'*20}\nVocê digitou os valores {valores}")
