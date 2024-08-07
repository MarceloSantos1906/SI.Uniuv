'''
Marcelo dos Santos Junior

Exercicio 4: Escreva uma função que recebe uma lista de números como parâmetro e retorna uma nova
lista com os números pares da lista original

'''
import random
lista = []
par = []
def something():
    for i in range (7):
        #valor = int(input("Insira um valor: "))
        valor = random.randint(0,10000)
        lista.append(valor)

    for k in range (len(lista)):
        if lista[k] % 2 == 0:
            par.append(lista[k])
    return par

something()
print(f"Lista de pares: {par}")
print(f"Lista original: {lista}")