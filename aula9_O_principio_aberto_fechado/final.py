class Artista:
    def __init__(self, tipo : str) -> None:
        self.tipo = tipo
    def apresentar_show(self):
        print(f"O {self.tipo} está apresentando seu show!")

class Circo:
    def apresentar(self, artista : Artista) -> None:
        print(f"O circo está abrindo!")
        artista.apresentar_show()
        print(f"O público aplaude!")

circo = Circo()
artista = Artista("mímico")
circo.apresentar(artista)