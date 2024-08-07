'''
Marcelo dos Santos Junior

Exercicio 12 : 

Faça um programa que simula uma calculadora que aceita as seguintes operações: soma,
subtração, divisão e multiplicação. O programa inicia pedindo para o usuário escolher uma
opção do menu

1. Somar
2. Subtrair
3. Dividir
4. Multiplicar
5. Sair

Ao escolher a opção, o programa solicita os dois números a serem operados (exceto se a
opção escolhida for a 5), efetua a operação, mostra o resultado na tela e volta para o menu
para que o usuário escolha outra opção

'''

while True:
    print("1. Somar \n2. Subtrair \n3. Dividir \n4. Multiplicar \n5. Sair")
    opcao = int(input("digite uma das opções: "))
    if opcao == 5:
        exit()
    elif opcao == 1:
        val1 = int(input("digite o primeiro valor: "))
        val2 = int(input("digite o segundo valor: "))
        conta = val1+val2
        print("a soma é: ", conta, "\n")
    elif opcao == 2:
        val1 = int(input("digite o primeiro valor: "))
        val2 = int(input("digite o segundo valor: "))
        conta = val1-val2
        print("a subtração é: ", conta, "\n")
    elif opcao == 3:
        val1 = int(input("digite o primeiro valor: "))
        val2 = int(input("digite o segundo valor: "))
        conta = val1/val2
        print("a divisão é: ", conta, "\n")
    elif opcao == 4:
        val1 = int(input("digite o primeiro valor: "))
        val2 = int(input("digite o segundo valor: "))
        conta = val1*val2
        print("a multiplicação é: ", conta, "\n")
    else:
        print("opção invalida \n")