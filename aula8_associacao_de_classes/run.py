class Interruptor:
    def __init__(self, comodo : str):
        self.comodo = comodo
    def acender(self) -> None:
        print(f"Estou acendendo a luz do comodo: {self.comodo}")
    def apagar(self) -> None:
        print(f"Estou apagando a luz do comodo: {self.comodo}")

class Pessoa:
    def acender_luzes(self, interruptor : Interruptor) -> None:
        interruptor.acender()
    def apagar_luzes(self, interruptor : Interruptor) -> None:
        interruptor.apagar()
    def dormir(self) -> None:
        print(f"A pessoa foi dormir.")

agnaldo = Pessoa()
interruptor_sala = Interruptor("sala")
interruptor_quarto = Interruptor("quarto")

agnaldo.acender_luzes(interruptor_sala)
agnaldo.apagar_luzes(interruptor_quarto)
agnaldo.dormir()
