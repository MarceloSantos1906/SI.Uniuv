'''
3 exercicio

Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do
usuário e escreva essas informações

'''

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura em centimetros: "))
peso = float(input("Insira seu peso: "))
nacionalidade = input("Insira sua nacionalidade: ")

print("Seu nome é " + nome + " voce tem ", idade, " anos, ", altura, " centimetros de altura, seu peso é ", peso, " kilos sua nacionalidade é ", nacionalidade)