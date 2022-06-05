#O código abaixo resultará em erro pois o método digaOla da classe Admin está tentando
#chamar uma propriedade privada da classe Usuario

class Usuario():
    __nomeUsuario=""

    def setUsuario(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario

class Admin(Usuario):

    def escrevaNome(self):
        return "Admin"
    
    def digaOla(self):
        return f"Olá, admin {self.__nomeUsuario}"

admin1=Admin()
admin1.setUsuario("Baltazar")
print(admin1.digaOla())

#Codigo corrigido:

class Usuario():
    _nomeUsuario=""

    def setUsuario(self, nomeUsuario):
        self._nomeUsuario = nomeUsuario

class Admin(Usuario):

    def escrevaNome(self):
        return "Admin"
    
    def digaOla(self):
        return f"Olá, admin {self._nomeUsuario}"

admin1=Admin()
admin1.setUsuario("Baltazar")
print(admin1.digaOla())

#Com o método getter:

class Usuario():
    _nomeUsuario=""

    def setUsuario(self, nomeUsuario):
        self._nomeUsuario = nomeUsuario
    def getUsuario(self):
        return f"{self._nomeUsuario}"


class Admin(Usuario):

    def escrevaNome(self):
        return "Admin"
    
    def digaOla(self):
        return f"Olá, admin {self._nomeUsuario}"

    def getUsuario(self):
        return f"O nome do admin é {self._nomeUsuario}"

admin1=Admin()
admin1.setUsuario("Baltazar")
print(admin1.getUsuario())