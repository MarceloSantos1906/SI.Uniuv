'''
Marcelo dos Santos Junior

Exercicio 2 : Faça um programa que receba do usuário uma lista com 5 posições. Em seguida deverá ser
impresso a soma do maior com o menor elemento da lista

'''
lista = []

for i in range (5):
    valor = int(input("Insira um valor: "))
    lista.append(valor)

maior = max(lista)
menor = min(lista)

soma = maior + menor

print("A soma do maior valor com o menor valor é ", soma)