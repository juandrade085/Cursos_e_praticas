def linha (tamanho = 42):
    return '~' * tamanho

def cabeçalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):