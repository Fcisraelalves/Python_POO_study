class Livro:
    def __init__(self, titulo : str, autor : str, ano : int) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
    def exibir_dados(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Ano: {self.__ano}")

domCasmurro = Livro("Dom Casmurro", "Machado de Assis", 1899)
domCasmurro.exibir_dados()        