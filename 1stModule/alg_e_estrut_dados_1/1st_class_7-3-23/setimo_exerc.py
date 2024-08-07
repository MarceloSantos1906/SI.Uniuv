'''
exercicio 7

Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendose que o preço do combustível é de R$ 1,90, escreva um programa 
para ler: a marcação do odômetro (Km) no início do dia, a marcação (Km) no final do dia, o
número de litros de combustível gasto e o valor total (R$) recebido dos passageiros.
Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia

'''

combustivel = 1.9

def consumo_combustivel():
    odometro_inicio = int(input("Insira o km inicial: "))
    odometro_final = int(input("Insira o km final: "))
    if odometro_final < odometro_inicio:
        print("Valor invalido tente novamente")
        consumo_combustivel()
    else:
        consumo_combustivel2(odometro_final,odometro_inicio)

def consumo_combustivel2(odometro_final,odometro_inicio):
    combustivel_gasto = int(input("Insira a quantidade de combustivel gasto: "))
    valor_recebido = float(input("Insira o valor total recebido: "))
    if combustivel_gasto < 0 or valor_recebido < 0:
        print("Valor invalido tente novamente")
        consumo_combustivel2()
    else:
        km_ = odometro_final-odometro_inicio
        media_consumo = km_/combustivel_gasto
        media_consumo_valor = media_consumo*combustivel
        lucro = valor_recebido - media_consumo_valor
        print("A media do consumo foi de %2.f" % media_consumo, "Km/L e teve um lucro total de R$%2.f" % lucro)

consumo_combustivel()