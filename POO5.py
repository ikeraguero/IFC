class Usuario():
    __primeiroNome=""
    __ultimoNome=""

    def __init__(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def getNomeCompleto(self):
        return "O nome completo do usuário é " + self.__primeiroNome + " " + self.__ultimoNome

Usuario1 = Usuario("Charles", "Leclerc")
print (Usuario1.getNomeCompleto())