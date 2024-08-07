matriz = []

for i in range(3):
    linha = []
    for k in range(3):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz.append(linha)

menor = matriz[0][0]

for i in range(3):
    for j in range(3):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_l = i
            pos_c = j

print(f"O menor valor é {matriz[pos_l][pos_c]} na posição [{i},{j}]")