'''
Marcelo dos Santos Junior

Exercicio 5: Escreva uma função que recebe uma lista de palavras como parâmetro e retorna uma nova
lista com as palavras que têm pelo menos 5 letras

'''
import random
lista = []
maior5 = []

def something():
    for i in range (7):
        palavra = input("Insira um valor: ")
        lista.append(palavra)

    for k in range (len(lista)):
        if len(lista[k]) >= 5:
            maior5.append(lista[k])
    return maior5

something()

print(f"Lista com palavras com mais de 5 letras: {maior5}")
print(f"Lista original: {lista}")