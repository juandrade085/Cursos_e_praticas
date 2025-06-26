from ex115.lib.interface import cabeçalho


def arquivoExiste (nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except Exception as erro:
        print(f'Houve um ERRO na criação do arquivo!Erro: {erro}')
    else:
        print(f'Arquivo {nome} criado com sucesso!!!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'Houve um ERRO ao ler o arquivo!Erro: {erro}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a: #pra cada linha no arquivo
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<3} anos')

    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'Houve um ERRO na abertura do arquivo!Erro: {erro}')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except Exception as erro:
            print(f'Houve um ERRO ao escrever os dados!Erro: {erro}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
