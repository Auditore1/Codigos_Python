class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self,valor):
        if valor < 0:
            print("Só pode depositar valores positivos")
        else:
            self.__saldo += valor

    def sacar(self,valor):
        if valor > self.__saldo:
            print("Seu saldo é inferior ao valor desejado")
        else:
            self.__saldo -= valor
        print(f"Valor retirado!! Resta: {self.__saldo}")

    def getSaldo(self):
        print(f"Seu saldo é: {self.__saldo}") 



#Outra forma de criar Getters e Setters
class Conta2:
    def __init__(self, numero, titular, saldo, limite = 1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Decoradores
    #Exibir o saldo
    @property 
    def saldo(self):
        return f"O seu saldo é: R${self.__saldo}"
    
    #Inserir valores no atributo
    @saldo.setter
    def saldo(self,valor):
        if valor < 0:
            print("Você não pode depositar valores negativos!")
        else:
            self.__saldo+= valor
            print("Valor depositado com sucesso!!")