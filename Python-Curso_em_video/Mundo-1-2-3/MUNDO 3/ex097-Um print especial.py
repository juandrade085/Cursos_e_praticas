"""Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem com
tamanho adaptável."""

def escreva(texto):
    tam = len(texto)+4
    print(f"{'~'*tam}\n"
          f"{texto:^{tam}}\n"
          f"{'~'*tam}\n")

frase = str(input(f'Frase: '))
escreva(frase)