'''
Marcelo dos Santos Junior

Exercicio 6: 
Crie uma classe chamada "ContaBancaria" com os atributos "self.numeroDaConta" , "self.saldo" e
“self.limite”. Crie um método chamado "depositar" que recebe um valor e adiciona esse valor ao
self.saldo da conta, Crie um método chamado “aumentarself.limite” que recebe um novo valor de
self.limite e Crie outro método chamado "sacar" que recebe um valor e subtrai esse valor do
self.saldo da conta, desde que o self.saldo não fique abaixo de zero ou do self.limite. Crie uma instância
dessa classe e teste os métodos "depositar" e "sacar"

'''

class ContaBancaria:
    def __init__(self):
        self.numeroDaConta = 0
        self.aumentolimite = 0
        self.saldo = 0
        self.limite = 0
        self.saldo_ = 0
    def depositar(self):
        self.saldo_ = int(input("\nInsira o valor a adicionar: "))
        return self.saldo_
    def sacar(self):
        self.saldo_ = int(input("\nInsira o valor a sacar: "))
        return self.saldo_
    def aumentarlimite(self,limite,numeroDaConta,saldo):
        self.aumentolimite = int(input("\nValor a aumentar: "))
        return self.aumentolimite

numeroDaConta = 0
aumentolimite = 0
saldo = 0
limite = 0
saldo_ = 0

while True:
    print("1. Depositar \n2. Sacar \n3. Aumentar limite")
    funcao = input("Qual função deseja utilizar? ")
    if funcao == "1":
        saldo += ContaBancaria().depositar()
        print(f"Conta: {numeroDaConta} Saldo: {saldo} Limite: {limite}\n")
    elif funcao == "2":
        if saldo <= 0 and limite == 0:
            print("\nsaldo e limite insuficiente \n")
            limite *= -1
            print(f"Conta: {numeroDaConta} Saldo: {saldo} Limite: {limite}\n")
            limite *= -1
        elif saldo == limite or (saldo == limite and saldo <= 0):
            print("\nsaldo e limite insuficiente")
            limite *= -1
            print(f"Conta: {numeroDaConta} Saldo: {saldo} Limite: {limite}\n")
            limite *= -1
        elif (saldo > limite and limite < 0) or saldo > 0:
            saldo_1 = saldo
            saldo -= ContaBancaria().sacar()
            if (saldo < limite and limite == 0) or (saldo < 0 and limite == 0) or (saldo < limite):
                print("\nsaldo e limite insuficiente")
                saldo = saldo_1
                limite *= -1
                print(f"Conta: {numeroDaConta} Saldo: {saldo} Limite: {limite}\n")
                limite *= -1
            elif (saldo >= limite and limite < 0) or saldo >= 0:
                limite *= -1
                print(f"Conta: {numeroDaConta} Saldo: {saldo} Limite: {limite}\n")
                limite *= -1
    elif funcao == "3":
        limite *= -1
        limite += ContaBancaria().aumentarlimite(limite, numeroDaConta, saldo)
        print(f"Conta: {numeroDaConta} Saldo: {saldo} Limite: {limite}\n")
        limite *= -1
    else: print("\nOpção invalida\n")
