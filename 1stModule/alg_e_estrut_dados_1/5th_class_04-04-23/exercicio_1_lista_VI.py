'''
Marcelo dos Santos Junior

Exercicio 1: Escreva uma função que recebe uma lista como parâmetro e retorna o maior número da lista

'''
import random

lista = []
maior = 0
maior_= 0

def maior_lista(maior):
    maior = lista[0]
    for k in range (len(lista)):
        if lista[k] > maior:
            maior = lista[k]
    return maior

for i in range (random.randint(0,1000000)):
    lista.append(random.randint(-1000000,1000000))

maior_ = maior_lista(maior)
print(f"O maior valor da lista é {maior_}")