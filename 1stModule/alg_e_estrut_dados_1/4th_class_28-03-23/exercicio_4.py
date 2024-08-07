'''
Marcelo dos Santos Junior

Exercicio 4 : Faça um programa para ler a nota da prova de 6 alunos e armazene em uma lista, calcule e
imprima a média geral

'''
lista = []
nomes = []
notas = []
media = 0

for i in range (6):
    nomes.append(input("Informe o nome do aluno: "))
    notas.append(float(input(f"Informe a nota de {nomes[i]} : ")))
    media += notas[i]

media = media / 6

print("A media da turma é: ", media)
