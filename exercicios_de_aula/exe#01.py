class ContaBancaria:
    def __init__(self, titular : str, saldo : float):
        self.__titular = titular
        self.__saldo = saldo
    def set_titular(self, titular : str):
        self.__titular = titular
    def get_titular(self) -> str:
        return self.__titular
    def set_saldo(self, saldo : float):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            raise ValueError("O valor do saldo não pode ser negativo.")
    def get_saldo(self) -> float:
        return self.__saldo
    def exibir_info(self):
        print(f"O titular é {self.get_titular()}.")
        print(f"O saldo da conta é {self.get_saldo()}.")
        

minha_conta = ContaBancaria("Israel", 0)
minha_conta.exibir_info()
minha_conta.set_saldo(1000)
minha_conta.exibir_info()

