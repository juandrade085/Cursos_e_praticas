# SISTEMA


from lib.modulos_uteis import cadastro as cad_paciente
from lib.modulos_uteis import decoracao as dec

# Exibe o cabeçalho decorado
print(dec(15, '-='))
print(f"{'CLÍNICA VIDA+':^30}")
print(dec(15, '-='))

# Realiza o cadastro do paciente
paciente = cad_paciente()

# Exibe os dados do paciente cadastrado
print(
    f"Paciente: {paciente['nome']} {paciente['sobrenome']}, "
    f"{paciente['idade']} anos e {paciente['dias_com_idade_nova']} dias — cadastrado com sucesso!"
)