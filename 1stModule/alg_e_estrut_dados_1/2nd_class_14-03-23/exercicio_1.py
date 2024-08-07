'''
Exercicio 1

1. Escreva um programa que leia o código de origem de um produto e imprima na tela
a região de sua procedência conforme a tabela abaixo:

Observação: Caso o código não seja nenhum dos especificados o produto deve ser
encarado como importado

'''


codigo_origem = int(input("Insira o codigo de origem (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ou 11): "))

if codigo_origem == 1:
    print("O produto originou no Sul")

elif codigo_origem == 2:
    print("O produto originou no Norte")

elif codigo_origem == 3:
    print("O produto originou no Leste")

elif codigo_origem == 4:
    print("O produto originou no Oeste")

elif codigo_origem == 5 or codigo_origem == 6:
    print("O produto originou no Nordeste")

elif codigo_origem == 7 or codigo_origem == 8 or codigo_origem == 9:
    print("O produto originou no Suldeste")

elif codigo_origem == 10:
    print("O produto originou no Centro-Oeste")

elif codigo_origem == 11:
    print("O produto originou no Noroeste")

else:
    print("O produto foi importado")
