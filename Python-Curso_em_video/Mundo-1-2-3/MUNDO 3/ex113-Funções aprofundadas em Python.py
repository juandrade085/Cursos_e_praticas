"""Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


# Programa principal
numero_inteiro = leiaInt('Digite um número Inteiro: ')
numero_real = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {numero_inteiro} '
      f'e o real foi {numero_real}O')