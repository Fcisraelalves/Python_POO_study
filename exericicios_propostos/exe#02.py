class Livro:
    def __init__(self, titulo : str, autor : str, ano : int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")

domCasmurro = Livro("Dom Casmurro", "Machado de Assis", 1899)
domCasmurro.exibir_dados()        