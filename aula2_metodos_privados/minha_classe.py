class Pessoa:
    def __init__(self, altura : float, cpf : str):
        self.altura = altura
        self.__cpf = cpf
    def apresentar(self):
        print(f"Oiii, minha altura é {self.altura}")
        self.__mostrar_documento()
    def __mostrar_documento(self):
        print(f"Meu documento - {self.__cpf}")
        
fulano = Pessoa(1.80, 12020020302)

fulano.apresentar()