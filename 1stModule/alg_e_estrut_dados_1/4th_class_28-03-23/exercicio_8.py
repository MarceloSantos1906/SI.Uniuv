'''
Marcelo dos Santos Junior

Exercicio 8 : Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos
valores diferentes existem no vetor

'''
lista = []

for i in range (10):
    lista.append(int(input("Informe um valor: ")))

diferentes = len(set(lista))

print(lista)
print(diferentes)