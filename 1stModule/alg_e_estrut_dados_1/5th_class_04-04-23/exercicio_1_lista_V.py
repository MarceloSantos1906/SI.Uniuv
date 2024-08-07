'''
Marcelo dos Santos Junior

Exercicio 1: Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui

'''
matriz = []
maior = 0

for i in range(4):
    linha = []
    for k in range(4):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz.append(linha)
print(matriz)

for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            maior += 1
print(f"a matriz contem {maior} valores maiores que 10")