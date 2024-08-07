'''
Marcelo dos Santos Junior

Exercicio 6 : Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o
maior e o menor valor

'''
lista = []
pos_maior = 0
pos_menor = 0

for i in range (5):
    lista.append(int(input("Informe um valor: ")))

maior = lista[0]
menor = lista[0]

for k in range (len(lista)):
    if lista[k] > maior:
        maior = lista[k]
        pos_maior = k

for q in range (len(lista)):
    if lista[q] < menor:
        menor = lista[q]
        pos_menor = q

print(f"O maior valor da lista é {maior} no indice {pos_maior} e o menor valor da lista é {menor} no indice {pos_menor}")