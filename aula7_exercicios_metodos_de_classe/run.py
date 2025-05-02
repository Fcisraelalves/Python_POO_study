class Loja:
    
    taxa = 1.15
    
    def __init__(self, valor_produto_bruto : float) -> None:
        self.valor_produto_bruto = valor_produto_bruto
    
    def consultar_valor_do_produto(self) -> float:
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f"Valor do produto: {valor_produto : .2f}")
    
    @classmethod
    def editar_taxa_do_produto(cls, taxa : float):
        cls.taxa = taxa

loja_praia = Loja(32.99)
loja_shopping = Loja(21.99)
loja_rua = Loja(10.99)

loja_praia.consultar_valor_do_produto()
loja_shopping.consultar_valor_do_produto()
loja_rua.consultar_valor_do_produto()

loja_praia.editar_taxa_do_produto(1.55)

print("EDITEI A TAXA!!!")

loja_praia.consultar_valor_do_produto()
loja_shopping.consultar_valor_do_produto()
loja_rua.consultar_valor_do_produto()