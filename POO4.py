#2

class Usuario():
    __primeiroNome=""

    def setUsuario(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getUsuario(self):
        return ("O nome do usuario é " + self.__primeiroNome)

Usuario1 = Usuario()
Usuario1.setUsuario("Joe")

print(Usuario1.getUsuario())

#3

class Empregado():
    nome=""
    __salario=""
    projeto=""

    def setSalario(self, salario):
        self.__salario = salario

    def setNome(self, nome):
        self.nome = nome

    def setProjeto(self, projeto):
        self.projeto = projeto
    
    def trabalho(self):
        return ("O empregado se chama " + self.nome + " e está trabalhando no projeto " + self.projeto)
    
    def mostrar(self):
        return("Nome do empregado: " + self.nome + ". Salário: " + self.__salario)

Empregado1 = Empregado()
Empregado1.setNome("Iker")
Empregado1.setSalario("R$10.000")
Empregado1.setProjeto("Childcare Brasil")

print(Empregado1.trabalho())
print(Empregado1.mostrar())

#4

class Robo():
    __nome=""
    __ano_construcao=""

    def diga_alo(self):
        return ("Olá, eu me chamo " + self.__nome)
    def setNome(self, nome):
        self.__nome=nome
    def setAnoConstrucao(self, ano_construcao):
        self.__ano_construcao=ano_construcao
    def getAnoConstrucao(self):
        return ("Fui construido no ano de " + self.__ano_construcao)
    
Robo1 = Robo()
Robo1.setNome("Richard")
Robo1.setAnoConstrucao("1970")
print (Robo1.diga_alo())
print(Robo1.getAnoConstrucao())

#5

class Laptop():
    __preco=""

    def getPreco(self):
        return ("O Laptop custa: " + self.__preco)
    def setPreco(self, preco):
        self.__preco = preco

Laptop1 = Laptop()
Laptop1.setPreco("R$3.999")
print (Laptop1.getPreco())

#6

class Pessoa():
    __primeiroNome=""
    __segundoNome=""

    def getPrimeiroNome(self):
        return ("O primeiro nome desta pessoa é " + self.__primeiroNome)
    def getSegundoNome(self):
        return ("e seu segundo nome é " + self.__segundoNome)
    def setPirmeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome
    def setSegundoNome(self, segundoNome):
        self.__segundoNome = segundoNome

Pessoa1 = Pessoa()
Pessoa1.setPirmeiroNome("João")
Pessoa1.setSegundoNome("Carvalho")
print(Pessoa1.getPrimeiroNome())
print(Pessoa1.getSegundoNome())
