class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    def obter_saldo(self):
        return self.__saldo


# Certifique-se de que a definição da classe está completa antes de usar a classe
contJoao = ContaBancaria("João", 1000)

print(contJoao.titular)
print(contJoao.obter_saldo())  # Use o método obter_saldo para acessar o saldo


contJoao.depositar(2500)
print(contJoao.obter_saldo())


#intervalo 

contJoao.sacar(500)
print(contJoao.obter_saldo())