def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = input(msg).strip().replace(',', '.')
        # Verifica se são apenas número e se tem mais de um ponto
        if entrada.count('.') <= 1 and entrada.replace('.', '').isnumeric():
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')

