#Transformando módulos em pacotes

"""Adicione o módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(), que mostre na tela algumas informações geradas
pelas funções que já temos no módulo criado até aqui."""

from ex111.utilidadescev import moeda

valor = float(input('Digite o preço : R$ '))
moeda.resumo(valor, 20, 12)
