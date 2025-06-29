"""Crie um módulo chamado moeda.py que tenha as funçoes_questoes
incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um
programa que importe esse módulo e use algumas dessas funçoes_questoes."""

import moeda

valor = float(input('Digite o preço : R$ '))
aumento = float(input('Qual seria o aumento?(%) '))
desconto = float(input('Qual seria o desconto?(%) '))
print(f'A metade de {valor} é {moeda.metade(valor)};\n'
      f'O dobro de {valor} é {moeda.dobro(valor)};\n'
      f'Aumentando em {aumento}%, temos R$ {moeda.aumentar(valor, aumento)} e\n'
      f'Reduzindo em {desconto}%, temos R$ {moeda.diminuir(valor, desconto)}.')