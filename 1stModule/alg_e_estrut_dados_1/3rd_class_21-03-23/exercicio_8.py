'''
Marcelo dos Santos Junior

Exercicio 8 : Faça um programa onde o usuário digita 6 valores e imprima a soma destes valores na tela

'''

valores = []
soma = 0

for i in range(0, 6, 1):
    a = int(input("insira um valor para a soma: "))
    valores.append(a)

soma = sum(valores)

print("a soma é :", soma)