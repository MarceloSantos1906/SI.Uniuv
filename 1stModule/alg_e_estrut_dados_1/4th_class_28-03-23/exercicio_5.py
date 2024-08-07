'''
Marcelo dos Santos Junior

Exercicio 5 : Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o
maior e o menor valor

'''
lista = []

for i in range (5):
    lista.append(int(input("Informe um valor: ")))

maior = lista[0]

for k in range (len(lista)):
    if lista[k] > maior:
        maior = lista[k]
        pos = k

print(f"O maior valor da lista é {maior} no indice {pos}")