'''
Marcelo dos Santos Junior

Exercicio 5: Escreva um programa que receba uma matriz de tamanho n x m e calcule a soma de cada
linha e coluna

'''

matriz1 = []
colunas = int(input("Digite a largura da matriz: "))
linhas = int(input("Digite a altura da matriz: "))
soma_linhas = [0]*linhas
soma_colunas = [0]*colunas

for i in range(linhas):
    linha_ = []
    for k in range(colunas):
        linha_.append(int(input(f"Digite o valor [{str(i)},{str(k)}]: ")))
    matriz1.append(linha_)

for i in range(linhas):
        print(f"A matriz é {matriz1[i]}")

for i in range(linhas):
    for j in range(colunas):
        soma_linhas[i] += matriz1[i][j]
        soma_colunas[j] += matriz1[i][j]

for i in range(linhas):
    print(f"Soma da linha {i}: {soma_linhas[i]}")
for j in range(colunas):
    print(f"Soma da coluna {j}: {soma_colunas[j]}")
