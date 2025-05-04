class ContaBancaria:
    def __init__(self, titular : str, saldo : float)-> None:
        self.__titular = titular
        self.__saldo = saldo
    
    @property
    def titular(self) -> str:
        return self.__titular
    @titular.setter
    def titular(self, titular : str):
        self.__titular = titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            raise ValueError("O valor do saldo não pode ser negativo.")
    
    def exibir_info(self):
        print(f"O titular da conta é {self.titular}.")
        print(f"O saldo da conta é {self.saldo}.")
        

minha_conta = ContaBancaria("Israel", 0)
minha_conta.exibir_info()
minha_conta.saldo = 2400
minha_conta.exibir_info()