'''
Marcelo dos Santos Junior

Exercicio 3 : Crie um programa que lê 6 valores inteiros e armazene em uma lista e, em seguida, mostre
na tela os valores lidos na ordem inversa

'''
lista = []

for i in range (6):
    valor = int(input("Insira um valor: "))
    lista.append(valor)

lista.reverse()

print(lista)