'''
exercicio 1

Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área.
Área = π.R²

'''

import math

pi = math.pi
raio = float(input("Insira o valor do raio: "))

area = (pi*(raio*raio))

print("A area é: ", area)