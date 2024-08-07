'''
Marcelo dos Santos Junior

Exercicio 3 : Faça um programa onde o usuário digita dez valores e imprima na tela a média destes
valores

'''
valores = []
i=1
soma = 0

while i <=10:
    a = int(input("insira um valor: "))
    valores.append(a)
    i += 1

media = sum(valores)/len(valores)

print("media : ",media)