'''
Exercicio 7

Faça um programa que converta um número inteiro positivo para a notação de
números romanos, considerando os seguintes símbolos romanos: I, V, X, L, C, D, M

'''

numeros = int(input("Insira o numero a ser convertido: "))

if numeros == 1:
    numero_convertido = "I"
    print("o numero em notação de números romanos é: ", numero_convertido)

elif numeros == 5:
    numero_convertido = "V"
    print("o numero em notação de números romanos é: ", numero_convertido)

elif numeros == 10:
    numero_convertido = "X"
    print("o numero em notação de números romanos é: ", numero_convertido)

elif numeros == 50:
    numero_convertido = "L"
    print("o numero em notação de números romanos é: ", numero_convertido)

elif numeros == 100:
    numero_convertido = "C"
    print("o numero em notação de números romanos é: ", numero_convertido)

elif numeros == 500:
    numero_convertido = "500"
    print("o numero em notação de números romanos é: ", numero_convertido)

elif numeros == 1000:
    numero_convertido = "M"
    print("o numero em notação de números romanos é: ", numero_convertido)
