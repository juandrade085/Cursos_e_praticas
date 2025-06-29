#Entrada de dados monetários

"""Adicione o módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(), que mostre na tela algumas informações geradas
pelas funçoes_questoes que já temos no módulo criado até aqui."""

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dados

valor = dados.leiaDinheiro('Digite o preço : R$ ')
moeda.resumo(valor, 20, 12)
