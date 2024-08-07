'''
exercicio 5

Faça um programa que lê um valor em reais e calcule o valor equivalente em dólares.
O usuário deve informar, além do valor em reais da compra, o valor da cotação do
dólar

'''
from forex_python.converter import CurrencyRates

c = CurrencyRates()

def conversao_real():
    valor_dolar = (c.get_rate('USD', 'BRL'))
    valor_compra = float(input("Insira o valor da compra: R$"))
    valor_convertido = valor_compra/valor_dolar
    print("O valor total da compra em dolares é $%.2f" % valor_convertido)
    continuar = input("Deseja fazer otra compra? s/n: ")
    if continuar == "s" or continuar == "sim":
        conversao_real()
    else:
        exit()

def conversao():
    valor_dolar = float(input("Insira o valor do dolar: $"))
    valor_compra = float(input("Insira o valor da compra: R$"))
    valor_convertido = valor_compra/valor_dolar
    print("O valor total da compra em dolares é $%.2f" % valor_convertido)
    continuar = input("Deseja fazer otra compra? s/n ")
    if continuar == "s" or continuar == "sim":
        conversao()
    else:
        exit()

opcao = input("Voce deseja usar o valor do dolar em tempo real? s/n: ")
if opcao == "s" or opcao == "sim":
    conversao_real()
else:
    conversao()