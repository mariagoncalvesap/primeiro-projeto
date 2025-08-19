usuarios = []  # Lista para guardar os usuários

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    usuarios.append({"nome": nome, "senha": senha})

    # salva no arquivo
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{senha}\n")

    print("Usuário cadastrado com sucesso!\n")

def fazer_login():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("✅ Login realizado com sucesso!\n")
            return
    print("❌ Usuário ou senha incorretos.\n")

# ---------------- PROGRAMA PRINCIPAL ----------------
print("=== Sistema de Cadastro e Login ===")

while True:
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        print("\n=== Usuários cadastrados ===")
        for u in usuarios:
            print(f"Nome: {u['nome']} | Senha: {u['senha']}")
        print()
    elif opcao == "4":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.\n")