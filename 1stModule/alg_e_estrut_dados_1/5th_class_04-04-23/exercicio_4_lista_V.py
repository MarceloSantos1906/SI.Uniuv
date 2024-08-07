'''
Marcelo dos Santos Junior

Exercicio 4: Faça um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A * B

'''
matriz1 = []
matriz2 = []
matriz3 = []

for i in range(3):
    linha = []
    for k in range(3):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz1.append(linha)

for i in range(3):
    linha = []
    for k in range(3):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz2.append(linha)

print("Primeira matriz:")
for i in range(3):
    print(matriz1[i])

print("Segunda matriz:")
for i in range(3):
    print(matriz2[i])

linha=[]
for i in range(3):
    linha=[]
    for j in range(3):
        valor = 0
        for k in range(3):
            valor += matriz1[i][k]*matriz2[k][j]
        linha.append(valor)
    matriz3.append(linha)

print("Terceira matriz:")
for i in range(3):
    print(matriz3[i])