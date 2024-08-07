'''
Marcelo dos Santos Junior

Exercicio 3: 
Crie uma classe chamada "ContaBancaria" com os atributos "titular" e "saldo". Crie um
método chamado "depositar" que recebe um valor e adiciona esse valor ao saldo da conta.
Crie outro método chamado "sacar" que recebe um valor e subtrai esse valor do saldo da
conta, desde que o saldo não fique abaixo de zero. Crie uma instância dessa classe e teste os
métodos "depositar" e "sacar"

'''
class ContaBancaria:
    def depositar(titular,saldo_):
        saldo_ = int(input("Insira o valor a adicionar: "))
        return saldo_
    def sacar(titular,saldo_):
        saldo_ = int(input("Insira o valor a sacar: "))
        return saldo_
    saldo = 0
    saldo_ = 0
    while True:
        titular = "Marcelo"
        print("1. Depositar \n2. Sacar")
        funcao = input("Qual função deseja utilizar? ")
        if funcao == "1":
            saldo += depositar(titular,saldo_)
            print(f"{titular} saldo: {saldo}\n")
        elif funcao == "2":
            if saldo <= 0: print("Saldo insuficiente \n")
            else:
                saldo_1 = saldo
                saldo -= sacar(titular,saldo_)
                if saldo < 0:
                    print("Saldo insuficiente \n")
                    saldo = saldo_1
                elif saldo >= 0: print(f"{titular} saldo: {saldo}\n")
        else: print("Opção invalida\n")