def cadastro_paciente(nome, sobrenome, idade):
    nome = input("Nome do Paciente: ")
    sobrenome = input("Sobrenome do Paciente: ")
    idade = input("Idade do Paciente: ")


def decoração(tamanho, item):
    return tamanho * item


print(f"{decoração(15, '-=')}")
print(f"{'CLÍNICA VIDA+':^30}")
print(f"{decoração(15, '-=')}")
pacientes = cadastro_paciente
print(f'Paciente: {cadastro_paciente('primeiro_nome', 'sobrenome', 'idade')} cadastrado com sucesso!')
