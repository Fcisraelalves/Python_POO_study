class Funcionario:
    total_funcionarios = 0
    def __init__(self, nome : str, cargo : str, salario : float) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        Funcionario.total_funcionarios += 1
    @classmethod
    def consultar_total_funcionarios(cls) -> int:
        return cls.total_funcionarios
    
print(Funcionario.consultar_total_funcionarios())
ana = Funcionario("Ana", "Contadora", 5760.76)
carla = Funcionario("Carla", "Engenheira de Produção", 8570.87)
israel = Funcionario("Israel", "Engenheiro de Mecatrônica", 12221.98)
print(Funcionario.consultar_total_funcionarios())
