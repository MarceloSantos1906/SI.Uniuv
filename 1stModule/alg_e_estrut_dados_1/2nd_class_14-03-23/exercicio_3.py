'''
Exercicio 3

Reescreva o programa do exercício anterior considerando o zero como neutro, ou
seja, se for digitado o valor zero, escrever a palavra zero

'''

valor = int(input("Insira um valor: "))

if valor == 0:
    print("O valor é 0")

elif valor % 2 == 0:
    print("O valor é positivo")

elif (valor % 2 != 0):
    print("O valor é negativo")