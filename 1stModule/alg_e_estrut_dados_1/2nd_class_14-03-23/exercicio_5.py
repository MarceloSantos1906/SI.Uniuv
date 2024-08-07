'''
Exercicio 5

Faça um programa que leia três coordenadas num espaço 2D e indique se formam
um triângulo, juntamente com o seu tipo (equilátero, isósceles e escaleno)

• Equilátero: todos os lados iguais
• Isósceles: dois lados iguais
• Escaleno: todos os lados diferentes

'''

base = float(input("Insira o valor da base do triangulo: "))
lado1 = float(input("Insira o valor de um dos lados do triangulo: "))
lado2 = float(input("Insira o valor do outro lado do triangulo: "))

if base == lado1 == lado2:
    print("Triangulo Equilátero")

elif (lado1 == lado2 and lado2 != base) or (base == lado1 and base != lado2) or (base == lado2 and base != lado1):
    print("Triangulo Isóceles")

elif (lado1 != lado2 and lado2 != base and lado1 != base) or (base != lado1 and base != lado2 and lado1 != lado2) or (base != lado2 and base != lado1 and lado1 != lado2):
    print("Triangulo Escaleno")
