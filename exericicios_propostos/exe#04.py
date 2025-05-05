class ContaBancaria:
    def __init__(self, saldo : float) -> None:
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, novo_saldo : float) -> None:
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            raise ValueError("O valor do saldo não pode ser negataivo.")
        
minha_conta = ContaBancaria(1000)
print(minha_conta.saldo)
minha_conta.saldo = 20000
print(minha_conta.saldo)


