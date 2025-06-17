"""Crie um programa que peça ao usuário uma senha.
O programa deve continuar pedindo até que o usuário digite a senha
correta (por exemplo, "1234")."""

while True:
    senha = input('Cadastre uma senha\n'
                  '- Com 4 dígitos;\n'
                  '- Todos números;\n'
                  '- Sem espaços;\n'
                  '>>>>')
    if senha.isnumeric() and len(senha) == 4:
            print('\033[0;30;42mSenha cadastrada com sucesso!✅\033[m')
            break
    else:
        print('\033[0;30;41mInválido! Tente novamente.\033[m')
