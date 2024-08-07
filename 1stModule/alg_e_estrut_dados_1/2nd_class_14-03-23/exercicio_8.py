'''
Exercicio 8

Escreva um programa que recebe como entrada a data de nascimento do usuário, e
informa qual o seu signo

'''

dia_nascimento = int(input("Insira seu dia de nacimento: "))
mes_nascimento = int(input("Insira seu mes de nacimento: "))

if dia_nascimento > 31 or mes_nascimento > 12:
    print("Valor Invalido")
    exit()

elif (dia_nascimento >= 21 and mes_nascimento == 3) or (dia_nascimento <= 20 and mes_nascimento == 4):
    print("Seu signo é Áries")

elif (dia_nascimento >= 21 and mes_nascimento == 4) or (dia_nascimento <= 20 and mes_nascimento == 5):
    print("Seu signo é Touro")

elif (dia_nascimento >= 21 and mes_nascimento == 5) or (dia_nascimento <= 20 and mes_nascimento == 6):
    print("Seu signo é Gêmeos")

elif (dia_nascimento >= 21 and mes_nascimento == 6) or (dia_nascimento <= 22 and mes_nascimento == 7):
    print("Seu signo é Câncer")

elif (dia_nascimento >= 23 and mes_nascimento == 7) or (dia_nascimento <= 22 and mes_nascimento == 8):
    print("Seu signo é Leão")

elif (dia_nascimento >= 23 and mes_nascimento == 8) or (dia_nascimento <= 22 and mes_nascimento == 9):
    print("Seu signo é Virgem")

elif (dia_nascimento >= 23 and mes_nascimento == 9) or (dia_nascimento <= 22 and mes_nascimento == 10):
    print("Seu signo é Libra")

elif (dia_nascimento >= 23 and mes_nascimento == 10) or (dia_nascimento <= 21 and mes_nascimento == 11):
    print("Seu signo é Escorpião")

elif (dia_nascimento >= 22 and mes_nascimento == 11) or (dia_nascimento <= 21 and mes_nascimento == 12):
    print("Seu signo é Sagitário")

elif (dia_nascimento >= 22 and mes_nascimento == 12) or (dia_nascimento <= 19 and mes_nascimento == 1):
    print("Seu signo é Carpicórnio")

elif (dia_nascimento >= 20 and mes_nascimento == 1) or (dia_nascimento <= 18 and mes_nascimento == 2):
    print("Seu signo é Aquário")

elif (dia_nascimento >= 19 and mes_nascimento == 2) or (dia_nascimento <= 20 and mes_nascimento == 3):
    print("Seu signo é Peixes")

else:
    print("Valor Invalido")