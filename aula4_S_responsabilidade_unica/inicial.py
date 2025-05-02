class SistemaCadastral:
    def cadastrar(self, nome : str, idade : int):
        if isinstance(nome, str) and isinstance(idade, int):
            print(f"Acessando o banco de dados...")
            print(f"Cadastrar usuário - {nome}, idade: {idade}.")
        else:
            print(f"Erro: dados inválidos.")