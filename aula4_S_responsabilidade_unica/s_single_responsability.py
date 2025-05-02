class SistemaCadastral:
    
    def cadastrar(self, nome : str, idade : int) -> None:
        if self.__validar_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__error_handle()
    
    def __validar_input(self, nome : str, idade : int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome : str, idade : int) -> bool:
        print("acessando banco de dados...")
        print(f"cadastrar usuário - {nome}, idade: {idade}.")
    
    def __error_handle(self):
        print(f"Erro: dados inválidos.")
        
sistema = SistemaCadastral()
sistema.cadastrar("israel", "17")