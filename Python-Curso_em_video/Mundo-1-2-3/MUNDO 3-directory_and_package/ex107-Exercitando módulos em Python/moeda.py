def aumentar(preço, aumento):
    #aumentar em %
    resultado = preço+(preço * (aumento / 100))
    return resultado

def diminuir(preço, desconto):
    #diminuir em %
    resultado = preço-(preço * (desconto / 100))
    return resultado

def dobro(preço):
    #dobrar
    resultado = preço * 2
    return resultado

def metade(preço):
    #metade
    resultado = preço / 2
    return resultado

