from modulos_uteis.funcoes_cadastro import cadastro as cadastro_paciente
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


"""def decoração(tamanho, item):
    return tamanho * item


print(f"{decoração(15, '-=')}")
print(f"{'CLÍNICA VIDA+':^30}")
print(f"{decoração(15, '-=')}")
pacientes = cadastro_paciente"""

pacientes = cadastro_paciente()
print(f"Paciente: {pacientes['nome']} {pacientes['sobrenome']}, {pacientes['idade']} anos e {pacientes['dias_com_idade_nova']} — cadastrado com sucesso!")
