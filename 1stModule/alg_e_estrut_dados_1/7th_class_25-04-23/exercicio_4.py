lista = []

for i in range (5):
    lista.append(int(input("Informe um valor: ")))

maior = lista[0]
menor = lista[0]
posmaior = 0
posmenor = 0

for i in range (len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posmaior = i

soma = sum(lista)
soma1 = lista[0]+lista[4]

print(f"Lista: {lista}")
print(f"A soma de todos os valores da lista é: {soma}")
print(f"O maior valor da lista é {maior} no indice {posmaior}")
print(f"A soma do primeiro e do ultimo valor é: {soma1}")