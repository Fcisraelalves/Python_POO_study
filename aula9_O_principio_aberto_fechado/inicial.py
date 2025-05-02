class Circo:
    def apresentar(self, command : int) -> None:
        if command == 1:
            self.__show_palhaco()
        if command == 2:
            self.__show_malabarista()
        if command == 3:
            self.__show_magico()
        
    def __show_palhaco(self):
        print(f"O palhaco está apresentando o seu show!")
    def __show_malabarista(self):
        print(f"O malabarista está apresentando o seu show!")
    def __show_magico(self):
        print(f"O mágico está apresentando o seu show!")
    
meu_circo = Circo()
meu_circo.apresentar(1)