class Usuario:
    primeiroNome=""
    segundoNOme=""

    def hello(self):
        return "Olá eu me chamo " + self.primeiroNome + self.segundoNome


Usuario1=Usuario()

Usuario1.primeiroNome="Iker"
Usuario1.segundoNome="Aguero"


print (Usuario1.hello())