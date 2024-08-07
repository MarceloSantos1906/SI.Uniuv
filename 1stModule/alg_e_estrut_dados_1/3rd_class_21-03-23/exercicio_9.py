'''
Marcelo dos Santos Junior

Exercicio 9 : Elabore um programa que leia n valores e mostre a soma de seus quadrados

'''

valores = []

repeticoes = int(input("numero de valores: "))
for i in range(0, repeticoes, 1):
    a = int(input("insira um valor para a soma: "))
    quadrado = a*a
    valores.append(quadrado)

print("o quadrado dos valores são: ", valores)