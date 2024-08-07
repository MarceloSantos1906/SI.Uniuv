'''
exercicio 6

Escreva um programa para ler as dimensões de uma cozinha retangular
(comprimento, largura e altura), calcular e escrever a quantidade de caixas de
azulejos para se colocar em todas as suas paredes (considere que não será
descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1,5
m2

'''

def azulejos_():
    comprimento = float(input("Insira o comprimento do comodo: "))
    largura = float(input("Insira a largura do comodo: "))
    altura = float(input("Insira a altura do comodo: "))
        
    if comprimento or largura or altura <= 0:
        print("Valor invalido, tente novamente")
        azulejos_()
    else:
        area = largura*comprimento
        azulejos = area/1.5
        print("Será necessario %2.f" % azulejos, "azulejos de 1.5m²")

azulejos_()