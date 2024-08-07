'''
Exercicio 2

Escreva um programa para ler um valor e escrever se é positivo ou negativo.
Considere o valor zero como positivo

'''

valor = int(input("Insira um valor: "))

if (valor % 2 == 0) or valor == 0:
    print("O valor é positivo")

elif (valor % 2 != 0):
    print("O valor é negativo")