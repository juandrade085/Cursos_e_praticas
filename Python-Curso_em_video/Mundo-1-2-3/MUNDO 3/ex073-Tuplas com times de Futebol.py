"""Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética
d) Em que posição na tabela está o time da Fortaleza"""

time = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
        'São Paulo', 'Corinthians', 'Bahia',	'Cruzeiro',	'Vasco',
        'Vitória', 'Atlético-MG',	'Fluminense', 'Grêmio',	'Juventude',
        'Red Bull Bragantino', 'Athletico-PR', 'Criciúma',	'Atlético-GO',
        'Cuiabá')
divisão = '=-'*20
print(divisão)
print(f'Lista do time do Brasileirão 2024: {time}')
print(divisão)
print(f'Os 5 primeiros são {time[:5]}') #a
print(divisão)
print(f'Os 4 últimos são {time[-4:]}') #b
print(divisão)
print(f'Times em ordem alfabética: {sorted(time)}') #c
print(divisão)
print(f'O Fortaleza está na {time.index('Fortaleza') + 1}ª posição.') #d
