def aumentar(preço=0, aumento=0, formato=False):
    """
    Calcula o valor com aumento percentual aplicado.

    Parâmetros:
    :param preço: (float ou int) Valor original do produto ou serviço.
    :param aumento: (float ou int) Percentual (%) de aumento a ser aplicado.
    :param formato: (bool) Se True, retorna o valor formatado como moeda.
                           Se False, retorna o valor bruto (float).

    Retorno:
    :return: Valor final após aplicar o aumento, com ou sem formatação de moeda.
    """
    resultado = preço + (preço * (aumento / 100))
    return resultado if not formato else moeda(resultado)

def diminuir(preço = 0, desconto = 0, formato = False):
    """
    Calcula o valor com desconto percentual aplicado.

    Parâmetros:
    :param preço: (float ou int) Valor original do produto ou serviço.
    :param desconto: (float ou int) Percentual (%) de desconto a ser aplicado.
    :param formato: (bool) Se True, retorna o valor formatado como moeda.
                           Se False, retorna o valor bruto (float).

    Retorno:
    :return: Valor final após aplicar o desconto, com ou sem formatação de moeda.
    """
    resultado = preço-(preço * (desconto / 100))
    return resultado if not formato else moeda(resultado)

def dobro(preço = 0, formato = False):
    """
    Calcula o dobro de um valor numérico.

    Parâmetros:
    :param preço: (float ou int) Valor que será duplicado.
    :param formato: (bool) Se True, retorna o valor formatado como moeda.
                          Se False, retorna um número simples (float).

    Retorno:
    :return: O dobro do valor informado, com ou sem formatação de moeda.
    """
    resultado = preço * 2
    return resultado if not formato else moeda(resultado)

def metade(preço = 0, formato = False):
    """
    Calcula a metade de um valor numérico.

    Parâmetros:
    :param preço: (float ou int) Valor que será dividido pela metade.
    :param formato: (bool) Se True, retorna o valor formatado como moeda.
                          Se False, retorna um número simples (float).
    Retorno:
    :return: A metade do valor, formatado como moeda se formato=True.
    """
    resultado = preço / 2
    return resultado if not formato else moeda(resultado)

def moeda(preço= 0, dinheiro = 'R$'):
    """
       Formata um número como valor monetário.

       Esta função recebe um número e o converte para uma string formatada no padrão de moeda,
       com duas casas decimais e vírgula como separador decimal.

       Parâmetros:
       :param preço: (float ou int) Valor numérico que será formatado como moeda. Ex: 49.9
       :param dinheiro: (str) Símbolo ou texto da moeda a ser exibido antes do valor. Ex: 'R$', '€', 'US$'

       Retorno:
       :return: (str) String com o valor formatado no padrão monetário. Ex: 'R$ 49,90'
       """
    return f'{dinheiro} {preço:.2f}'.replace('.',',')

def resumo (preço = 0, taxa_aumento = 10, taxa_redução = 5):
    """
    Exibe um resumo formatado com várias operações sobre um valor numérico.

    Parâmetros:
    :param preço: (float ou int) Valor que será analisado.
    :param taxa_aumento: (float ou int) Percentual (%) de aumento a ser aplicado.
    :param taxa_redução: (float ou int) Percentual (%) de desconto a ser aplicado.

    Esta função não retorna nenhum valor, apenas imprime os resultados no console.
    """
    print(f"{'-'*35}\n"
          f"{'RESUMO DO VALOR'.center(30)}\n"
          f"{'-'*35}\n"
          f"Preço Analisado: \t\t{moeda(preço)}\n"
          f"Dobro do Preço: \t\t{dobro(preço, True)}\n"
          f"Metade do Preço: \t\t{metade(preço, True)}\n"
          f"Com {taxa_aumento}% de aumento: \t{aumentar(preço, taxa_aumento, True)}\n"
          f"Com {taxa_redução}% de desconto: \t{diminuir(preço, taxa_redução, True)}\n"
          f"{'-'*35}\n")
