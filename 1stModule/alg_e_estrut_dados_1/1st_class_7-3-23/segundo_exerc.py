'''
exercicio 2

Escreva um programa para calcular e imprimir o número de lâmpadas necessárias
para iluminar um determinado cômodo de uma residência. Dados de entrada: a
potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em
metros) do cômodo. Considere que a potência necessária é de 18 watts por metro
quadrado

'''

potencia_lampada = int(input("Digite o valor da potencia das lampadas em watts: "))
largura_comodo = int(input("Digite a largura do comodo: "))
comprimento_comodo = int(input("Digite o comprimento do comodo: "))

area = (comprimento_comodo*largura_comodo)
print("Area total do comodo: ",area)

lampadas_ = (area*18)

lampadas_necessarias = lampadas_/potencia_lampada

print("Será necessario ", lampadas_necessarias,"lampadas")