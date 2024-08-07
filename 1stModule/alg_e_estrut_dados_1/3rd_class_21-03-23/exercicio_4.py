'''
Marcelo dos Santos Junior

Exercicio 4 : Faça um programa onde o usuário digita dez valores e imprima na tela quantos valores são
pares e quantos são ímpares.

'''

valores = []
i=1
par = 0
impar = 0

while i <=10:
    a = int(input("insira um valor: "))
    valores.append(a)
    if (a % 2 == 0):
        par += 1
    elif (a % 2 != 0):
        impar += 1
    i += 1

print(par, " numeros pares e ", impar, "numeros impares")