'''
Marcelo dos Santos Junior

Exercicio 9 : Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em
que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, o programa
deve imprimir o valor -1

'''
lista = []

for i in range (5):
    lista.append(int(input("Informe um valor: ")))
valor = int(input("Informe o valor que deseja encontrar: "))

if valor in lista:
    for k in range(len(lista)):
        if lista[k] == valor:
            index = k
    print(f"{valor} esta na posição {index} da lista")
else:
    print("-1")

print(lista)