'''
Marcelo dos Santos Junior

Exercicio 10 : 

Numa lanchonete, uma pessoa pode comprar Nuggets apenas em pacotes contendo 6, 9 ou
20 pedaços. 

Escreva um programa em Python que lê um valor inteiro num e que imprima
True se é possível comprar num Nuggets nessa lanchonete, ou Falso, caso contrário. 

Por exemplo, se num = 44, o programa deve retornar True (seria um pacote de 6, dois de 9 e 1
um de 20, por exemplo). Mas se num = 34, o programa deve retornar False

'''

num = int(input("digite quantos nuggets deseja comprar: "))

if num % 6 == 0 or num % 9 == 0 or num % 20 == 0:
    print("True")
    exit()

else:
    for i in range(num // 6):
        for j in range (num // 9):
            for k in range (num // 20):
                if i*6 + j*9 + k*20 == num:
                    print("True")
                    exit()
    print("False")
