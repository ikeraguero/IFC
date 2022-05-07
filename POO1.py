class Usuario:
    primeiroNome=""
    segundoNOme=""

    def hello(self):
        return "Olá eu me chamo " + self.primeiroNome + " " + self.segundoNome


Usuario1=Usuario()
Usuario2=Usuario()

Usuario1.primeiroNome=input("Digite o nome do usuário 1: ")
Usuario1.segundoNome=input("Digite o sobrenome do usuário 1: ")


Usuario2.primeiroNome="Jane"
Usuario2.segundoNome="Silva"

print ("Usuário 1: " + Usuario1.hello())
print ("Usuário 2: " + Usuario2.hello())