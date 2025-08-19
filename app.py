usuarios = []  #Lista para guardar usuários
print("=== Sistema de Cadastro de Usuários ===")
while True:
    nome = input ("Digite o nome do usuário: ")
    senha = input('Digite a senha')

    usuarios.append ({"nome": nome, "senha": senha})
    print("Usuário cadastrado com sucesso!\n")

    continuar = input ("Deseja cadastrar outro usuário? (s/n): ")
    if continuar.lower() != "s":

        print("\n=== Lista de Usuários Cadastrados ===")
        for u in usuarios:
            print(f"Nome: {u[ 'nome']} | Senha: {u['senha']}")