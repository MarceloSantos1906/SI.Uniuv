'''
Marcelo dos Santos Junior

Exercicio 1 : Leia uma lista de 7 posições. Contar e escrever quantos valores pares ele possui

'''

lista = []
par = 0
impar = 0

for i in range (7):
    valor = int(input("Insira um valor: "))
    lista.append(valor)

for k in range (len(lista)):
    if lista[k] % 2 == 0:
        par += 1
    elif lista[k] % 2 != 0:
        impar += 1

print(par, " numeros par e ", impar, "numeros impar")
print(lista)