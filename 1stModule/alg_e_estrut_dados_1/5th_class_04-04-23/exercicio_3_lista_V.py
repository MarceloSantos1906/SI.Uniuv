'''
Marcelo dos Santos Junior

Exercicio 3: Leia duas matriz1es 2 x 2 e escreva uma terceira com os maiores valores de cada
posição das matriz1es lidas

'''

matriz1 = []
matriz2 = []
matriz3 = []

for i in range(2):
    linha = []
    for k in range(2):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz1.append(linha)

maior = matriz1[0][0]

for i in range(2):
    for j in range(2):
        if matriz1[i][j] > maior:
            maior = matriz1[i][j]
            pos_l1 = i
            pos_c1 = j

print(f"O maior valor da primeira matriz é {matriz1[pos_l1][pos_c1]}")

for i in range(2):
    linha = []
    for k in range(2):
        linha.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz2.append(linha)

maior = matriz2[0][0]

for i in range(2):
    for j in range(2):
        if matriz2[i][j] > maior:
            maior = matriz2[i][j]
            pos_l2 = i
            pos_c2 = j

print(f"O maior valor da segunda matriz é {matriz2[pos_l2][pos_c2]}")

matriz3 = matriz1[pos_l1][pos_c1]*matriz2[pos_l2][pos_c2]

print(f"A terceira matriz é {matriz3}")