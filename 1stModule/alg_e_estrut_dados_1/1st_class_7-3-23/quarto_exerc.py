'''
4 exercicio

Faça um programa que lê o nome de um produto, a quantidade comprada, o valor
unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na
tela o nome do produto e o valor total da venda

'''


def compra():
    produto_comprado = input("Insira o nome do produto: ")
    quantidade_produtos = int(input("Insira a quantidade de produtos: "))
    valor_produto = float(input("Insira o valor do produto: "))
    porcetual_desconto = float(input("Insira o percentual de desconto: "))
    if porcetual_desconto <= 0:
        valor_total = (quantidade_produtos*valor_produto)
        print("O valor total da compra para ", quantidade_produtos, " ", produto_comprado," é: R$ %.2f" % valor_total)
        continuar = input("Deseja realizar mais uma compra? sim ou não: ")
        if continuar == "sim" or continuar == "s":
            compra()
        else:
            exit()
    else:
        desconto = (porcetual_desconto/100)
        valor_total = ((quantidade_produtos*valor_produto)-desconto)
        print("O valor total da compra para ", quantidade_produtos, " ", produto_comprado," é: R$ %.2f" % valor_total)
        continuar = input("Deseja realizar mais uma compra? sim ou não: ")
        if continuar == "sim" or continuar == "s":
            compra()
        else:
            exit()

compra()