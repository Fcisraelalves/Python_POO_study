class Celular:
    def __init__(self, modelo : str) -> None:
        self.modelo = modelo
    
    def enviar_mensagem(self, mensagem : str) -> None:
        print(f"Enviando mensagem: {mensagem}")
    def abrir_emails(self) -> None:
        print(f"Abrindo os Emails...")
    def abrir_youtube(self) -> None:
        print(f"Abrindo youtube...")
        
class Pessoa:
    def __init__(self, celular : Celular) -> None:
        self.celular = celular
    def pedir_pizza(self) -> None:
        print(f"Buscando o celular...")
        print(f"Definindo o sabor...")
        self.celular.enviar_mensagem("Quero uma portuguesa!")
        print("Aguardando chegada...")
    def estudar(self) -> None:
        print(f"Sentando no computador...")
        self.celular.abrir_youtube()
        print(f"Anotando o conteúdo...")

android = Celular("Samsung S22")
iphone = Celular("Iphone 13")

reginaldo = Pessoa(android)
mariscleia = Pessoa(iphone)

reginaldo.pedir_pizza()
print()
mariscleia.estudar()