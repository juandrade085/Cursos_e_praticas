"""Modifique as funções que form criadas no desafio 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado por elas
vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

import moeda

valor = float(input('Digite o preço : R$ '))
aumento = float(input('Qual seria o aumento?(%) '))
desconto = float(input('Qual seria o desconto?(%) '))
print(f"A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)};\n"
      f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)};\n"
      f"Aumentando em {aumento}%, temos {moeda.aumentar(valor, aumento, True)} e\n"
      f"Reduzindo em {desconto}%, temos {moeda.diminuir(valor, desconto, True)}.")