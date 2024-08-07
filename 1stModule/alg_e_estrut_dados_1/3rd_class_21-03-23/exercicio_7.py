'''
Marcelo dos Santos Junior

Exercicio 7 : Faça um programa que imprima na tela a soma dos valores de um intervalo definido pelo
usuário

'''

valor = int(input("insira um valor: "))
soma = 0

for i in range (1,valor, 1):
    soma += i
    print(i)
print("soma: ",soma)