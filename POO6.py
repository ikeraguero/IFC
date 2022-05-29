#BOLA

class Bola():
    __cor=""
    __circunferencia=""
    __material=""

    def __init__(self, cor, circunferencia, material):
        self.__cor=cor
        self.__circunferencia=circunferencia
        self.__material=material
    
    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return "Cor da bola: " + self.__cor

bola1 = Bola("Branca", 20, "papel")
bola1.trocaCor("Azul")
print(bola1.mostraCor())

#QUADRADO

class Quadrado():
    __tamanhoLado=""

    def __init__(self, tamanhoLado):
        self.__tamanhoLado = tamanhoLado
    
    def mudarLado(self, novoLado):
        self.__tamanhoLado = novoLado

    def calcularArea(self):
        return f"A área do quadrado é {self.__tamanhoLado*self.__tamanhoLado}"

    def retornarLado(self):
        return f"O tamanho do lado é {self.__tamanhoLado}"


quadrado1=Quadrado(10)
quadrado1.mudarLado(20)
print(quadrado1.retornarLado())
print(quadrado1.calcularArea())

#RETANGULO

class Retangulo():
    __base=""
    __altura=""

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def mudarDados(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura

    def retornarDados(self):
        return f"Altura: {self.altura}. Base: {self.base}"

    def calcularArea(self):
        return f"A área do retângulo é {self.base*self.altura}"

    def calcularPerimetro(self):
        return f"O perímetro do retâgulo é {(self.base*2)+(self.altura*2)}"

retangulo1=Retangulo(10,20)
retangulo1.mudarDados(10, 25)
print(retangulo1.calcularArea())
print(retangulo1.calcularPerimetro())


#CONTA CORRENTE

class ContaCorrente():
    __numeroConta=""
    __nomeCorrentista=""
    __saldo=""

    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.__numeroConta = numeroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

    def alterarNome (self, novoNome):
        self.nomeCorrentista = novoNome

    def saque(self, valorSaque):
        self.__saldo = self.__saldo - valorSaque

    def deposito(self, valorDeposito):
        self.__saldo = self.__saldo + valorDeposito
    
    def mostrarSaldo(self):
        return f"O saldo dessa conta é de R${self.__saldo}"

conta1=ContaCorrente(33, "Márcio", 100)
conta1.alterarNome("João")
conta1.saque(50)
conta1.deposito(100)
print (conta1.mostrarSaldo())

#TV

class TV():
    __volume=""
    __canal=""

    def __init__(self, volume, canal):
        self.__volume = volume
        self.__canal = canal

    def mudarCanal(self, novoCanal):
        self.__canal = novoCanal

    def aumentarVolume(self, valorAumento):
        self.__volume= self.__volume + valorAumento

    def diminuirVolume(self, valorDiminuir):
        self.__volume= self.__volume - valorDiminuir
    
    def mostrarVolume(self):
        return f"O volume da TV está em {self.__volume}"
    
    def mostrarCanal(self):
        return f"A TV está sintonizada no canal {self.__canal}"

tv1=TV(100, 37)
tv1.mudarCanal(4)
tv1.diminuirVolume(50)
tv1.aumentarVolume(20)
print(tv1.mostrarVolume())
print(tv1.mostrarCanal())

#FUNCIONÁRIO

class Funcionario():
    __nome=""
    __salario=""


    def __init__(self, nome, salario):
        self.nome= nome
        self.salario= salario

    def getNome(self):
        return f"O funcionário se chama {self.nome}"

    def getSalario(self):
        return f"Salário: R${self.salario}"

    def aumentarSalario(self, porcentagem):
        self.salario = self.salario + (self.salario*(porcentagem/100))

funcionario1=Funcionario("Iker", 1000)
print(funcionario1.getNome())
funcionario1.aumentarSalario(10)
print(funcionario1.getSalario())