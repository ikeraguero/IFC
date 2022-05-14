#1 
class Usuario:
    primeiroNome=""

    def hello(self):
        print ("Olá eu me chamo " + self.primeiroNome)
        return self
    def registrar(self):
        print ("Registrado!")
        return self
    def mail(self):
        print ("Email enviado!")

Usuario1=Usuario()
Usuario1.primeiroNome="Jane"

print("#EXERCICIO 1")
primeiroNome= Usuario1.hello().registrar().mail()

#2

class Carro:
    modelo=""

    def entrar_carro(self):
        print("O indivíduo entra em sua " + self.modelo)
        return self
    def ligar(self):
        print("O carro está sendo ligado")
        return self
    def dirigir(self):
        print("O carro está sendo dirigido")
        return self
    def frear(self):
        print("O carro está parando")
        return self
    def desligar(self):
        print("O carro está sendo desligado")
        return self

Ferrari = Carro()
Ferrari.modelo="Ferrari SF90 Spider"

print("#EXERCICIO 2")
modelo= Ferrari.entrar_carro().ligar().dirigir().frear().desligar()