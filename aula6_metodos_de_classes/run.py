class MinhaClasse:
    
    estatico = "lhama"
    
    def __init__(self, estado : bool):
        self.__estado = estado
    
    def print_variavel_de_classe(self):
        print(self.estatico)
    @classmethod
    def alterar_variavel_de_classe(cls):
        cls.estatico = "Alguma coisa"
        
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)

obj1.alterar_variavel_de_classe()

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
