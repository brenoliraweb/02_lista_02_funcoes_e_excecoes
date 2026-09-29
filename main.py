usuarios = [] # {'email': email, 'senha': senha}
alimentos = [] # {'titulo': titulo, 'preco': preco, 'descricao': descricao}

def cadastro_usuario():
    email = input('Digite seu e-mail: ').strip()
    senha = input('Digite sua senha: ').strip()

    if email == '' or senha == '':
        print('Preencha todos os campos!')
        return

    usuarios.append({'email': email, 'senha': senha})
    print('Usuário cadastrado!')

def login_usuario():
    email = input('E-mail: ').strip()
    senha = input('Senha: ').strip()

    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f'Bem-vindo(a), {email}')
            return True

    print('E-mail ou senha incorretos!')
    return False

def cadastrar_alimento():
    def verificar_titulo():
        while True:
            titulo = input('Digite o título: ').strip()

            if len(titulo) >= 2:
                return titulo

            print('Título precisa ter pelo menos 2 caracteres')

    def verificar_preco():
        while True:
            try:
                preco = float(input('Digite o preço: R$').replace(',', '.'))
            except ValueError:
                print('Digite um valor válido. Ex: 12.5')
                continue

            if preco <= 0:
                print('O preço deve ser maior que zero!')
                continue

            return preco

    def validar_descricao():
        while True:
            descricao = input('Digite a descrição: ').strip()

            if len(descricao) >= 5:
                return descricao

            print('Digite pelo menos 5 caracteres para a descrição ser válida.')

    alimento = {
        'titulo': verificar_titulo(),
        'preco': verificar_preco(),
        'descricao': validar_descricao()
    }

    alimentos.append(alimento)
    print('Alimento cadastrado!')

def listar_alimentos(alimentos):
    if len(alimentos) == 0:
        print('Nenhum alimento cadastrado.')
        return

    i = 1
    for alimento in alimentos:
        print(f'{i} - {alimento["titulo"]} | R${alimento["preco"]:.2f} | {alimento["descricao"]}')
        i += 1


logado = False

while True:
    try:
        print('[1] - Cadastrar usuário')
        print('[2] - Login')
        print('[3] - Cadastrar alimento')
        print('[4] - Listar alimentos')
        print('[5] - sair')

        opcao = int(input('Digite sua opção: '))

        if opcao == 1:
            cadastro_usuario()

        elif opcao == 2:
            logado = login_usuario()

        elif opcao == 3:
            if logado:
                cadastrar_alimento()
            else:
                print('Faça login primeiro!')

        elif opcao == 4:
            if logado:
                listar_alimentos(alimentos)
            else:
                print('Faça login primeiro!')

        elif opcao == 5:
            break

        else:
            print('Digite uma opção válida!')

    except ValueError:
        print('Erro: digite apenas números.')
