'''
Marcelo dos Santos Junior

Exercicio 7 : Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um
programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50
lançamentos

'''
import random

lista = []
num6 = 0

for i in range (50):
    valor = random.randint(0,6)
    lista.append(valor)

for k in range(len(lista)):
    if lista[k] == 6:
        num6 += 1

print(lista)
print(num6)

porc = num6/100*len(lista)
print("O numero 6 teve %2.f"%porc, "porcento de ocorrencias")