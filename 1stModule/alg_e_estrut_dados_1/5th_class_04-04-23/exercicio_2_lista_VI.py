'''
Marcelo dos Santos Junior

Exercicio 2: Escreva uma função que recebe uma lista de números como parâmetro e retorna a média
aritmética desses números

'''
import random

lista = []

def something(soma):
    for i in range (random.randint(0,1000000)):
        lista.append(random.randint(-1000000,1000000))
    for k in range (len(lista)):
        soma += lista[k]
    return soma

soma = 0
soma=something(soma)
media = soma/(len(lista))

print("A media é %2.f" % media)
