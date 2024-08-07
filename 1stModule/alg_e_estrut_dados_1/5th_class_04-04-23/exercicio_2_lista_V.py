'''
Marcelo dos Santos Junior

Exercicio 2: Leia uma matriz 2 x 2, imprima a matriz e retorne à localização (linha e a coluna) do
maior valor

'''
matriz = []

for i in range(2):
    linha = []
    for k in range(2):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz.append(linha)

maior = matriz[0][0]

for i in range(2):
    for j in range(2):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_l = i
            pos_c = j

print(f"O maior valor é {matriz[pos_l][pos_c]}")