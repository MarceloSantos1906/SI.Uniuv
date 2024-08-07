'''
Exercicio 4

Escreva um programa para ler 2 valores (considere que não serão informados valores
iguais) e escrever o maior deles

'''

valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))

if valor1 == valor2:
    print("Os valores são iguais")

elif valor1 > valor2:
    print("O primeiro valor  é maior")

elif valor1 < valor2:
    print("O segundo valor é maior")
