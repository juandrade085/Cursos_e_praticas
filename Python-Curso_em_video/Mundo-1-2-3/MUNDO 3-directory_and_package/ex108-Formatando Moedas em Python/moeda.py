def aumentar(preço = 0, aumento = 0):
    #aumentar em %
    resultado = preço+(preço * (aumento / 100))
    return resultado

def diminuir(preço = 0, desconto = 0):
    #diminuir em %
    resultado = preço-(preço * (desconto / 100))
    return resultado

def dobro(preço = 0):
    #dobrar
    resultado = preço * 2
    return resultado

def metade(preço = 0):
    #metade
    resultado = preço / 2
    return resultado

def moeda(preço= 0, dinheiro = 'R$'):
    return f'{dinheiro} {preço:.2f}'.replace('.',',')
