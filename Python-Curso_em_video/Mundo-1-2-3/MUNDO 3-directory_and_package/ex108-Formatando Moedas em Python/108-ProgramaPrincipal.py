"""Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números como um # valor monetário
formatado."""
from ex108 import moeda

valor = float(input('Digite o preço : R$ '))
aumento = float(input('Qual seria o aumento?(%) '))
desconto = float(input('Qual seria o desconto?(%) '))
print(f"A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))};\n"
      f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))};\n"
      f"Aumentando em {aumento}%, temos R$ {moeda.moeda(moeda.aumentar(valor, aumento))} e\n"
      f"Reduzindo em {desconto}%, temos R$ {moeda.moeda(moeda.diminuir(valor, desconto))}.")