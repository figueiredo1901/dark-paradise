usuario = input('Defina um nome de usuário: \n')
senha = input('Crie uma senha: \n')

while True:
    if usuario == senha:
        print('Usuário e senha iguais não são permitidos! Por favor, repita a operação.')
        usuario = input('Defina um nome de usuário: \n')
        senha = input('Crie uma senha: \n')
    else:
        print('Cadastro aceito. Bem-vindo!')
        break  # Sai do loop quando a senha for diferente do usuário
