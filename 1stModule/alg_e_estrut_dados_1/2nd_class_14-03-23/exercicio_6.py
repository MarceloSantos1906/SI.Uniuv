'''
Exercicio 6

As maçãs custam R$ 0,50 cada se forem compradas menos do que uma dúzia, e R$
0,40 se forem compradas pelo menos doze. Escreva um programa que leia o número
de maçãs compradas, calcule e escreva o valor total da compra

'''

macas = int(input("Insira o numero de maças comprada: "))

if macas >= 12:
    print("Valor total da compra: R$", macas*0.4)

elif macas < 12 and macas > 0:
    print("Valor total da compra: R$", macas*0.5)

else:
    print("Valor invalido")