class MinhaClasse:
    
    estatico = "lhama"
    
    def __init__(self, estado : bool) -> None:
        self.__estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "programador"
obj1.estatico = "olaMundo"
MinhaClasse.estatico = "lhamaAqui"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)

