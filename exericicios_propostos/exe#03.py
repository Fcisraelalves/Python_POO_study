class Livro:
    def __init__(self, titulo : str, autor : str, ano : int, estoque : int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        if estoque >= 0:
            self._estoque = estoque
        else:
            raise ValueError("O valor do estoque não deve ser negativo.")        
    def consultar_estoque(self):
        return self._estoque
    def atualizar_estoque(self, novo_valor : int):
        if novo_valor >= 0:
            self._estoque = novo_valor
        else:
            raise ValueError("O valor do estoque não deve ser negativo.")
    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")

domCasmurro = Livro("Dom Casmurro", "Machado de Assis", 1899, 20)
domCasmurro.exibir_dados()
print(f"Estoque: {domCasmurro.consultar_estoque()}")