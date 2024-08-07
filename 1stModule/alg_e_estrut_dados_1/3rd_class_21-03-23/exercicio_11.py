'''
Marcelo dos Santos Junior

Exercicio 11 : 

Foi realizada uma pesquisa em Niterói, com um número desconhecido de pessoas. De cada
entrevistado foram colhidos os seguintes dados:

1. Qual o seu clube de futebol de preferência (1 - Flamengo, 2 - Vasco, 3 - Fluminense, 4 - Botafogo, 5 - Outros)
2. Qual o seu salário
3. Qual a sua cidade natal (1 - Niterói, 2 - Outra)

Escreva um programa que informe:

• Número de torcedores por clube
• Média salarial dos torcedores de cada time
• Número de pessoas nascidas em Niterói e que não torcem para nenhum dos principais clubes do Rio
• Número de pessoas entrevistadas

'''
import time

repeticoes = 0
nsc_nit = 0
torcedores_fla = 0
torcedores_vas = 0
torcedores_flu = 0
torcedores_bot = 0
salario_fla = []
salario_vas = []
salario_flu = []
salario_bot = []

while True:
    print("times: \n1 - Flamengo \n2 - Vasco \n3 - Fluminense \n4 - Botafogo \n5 - Outros \n6 - Sair")
    times = int(input("A qual time você torce: "))
    if times == 1:
        salario = int(input("Qual o seu salario? "))
        salario_fla.append(salario)
        torcedores_fla += 1
        media_fla = sum(salario_fla)/len(salario_fla)
        print("a media salarial dos torcedores do Flamengo é: R$ %2.d" % media_fla)
        repeticoes += 1
    elif times == 2:
        salario = int(input("Qual o seu salario? "))
        salario_vas.append(salario)
        torcedores_vas += 1
        media_vas = sum(salario_vas)/len(salario_vas)
        print("a media salarial dos torcedores do Vasco é: R$ %2.d" % media_vas)
        repeticoes += 1
    elif times == 3:
        salario = int(input("Qual o seu salario? "))
        salario_flu.append(salario)
        torcedores_flu += 1
        media_flu = sum(salario_flu)/len(salario_flu)
        print("a media salarial dos torcedores do Flumunense é: R$ %2.d" % media_flu)
        repeticoes += 1
    elif times == 4:
        salario = int(input("Qual o seu salario? "))
        salario_bot.append(salario)
        torcedores_bot += 1
        media_bot = sum(salario_bot)/len(salario_bot)
        print("a media salarial dos torcedores do Botafogo é: R$ %2.d" % media_bot)
        repeticoes += 1
    elif times == 5:
        cidade = int(input("qual a sua cidade natal? 1 - Niterói, 2 - Outra: "))
        if cidade == 1:
            nsc_nit += 1
            print(nsc_nit, "pessoas nascindas no Niteroi")
        repeticoes += 1
    elif times == 6:
        print("a media salarial dos torcedores do Flamengo é: R$ %2.d" % media_fla)
        print("a media salarial dos torcedores do Vasco é: R$ %2.d" % media_vas)
        print("a media salarial dos torcedores do Flumunense é: R$ %2.d" % media_flu)
        print("a media salarial dos torcedores do Botafogo é: R$ %2.d" % media_bot)
        print(nsc_nit, "pessoas nascindas no Niteroi que não torcem para nenhum dos principais clubes do Rio")
        print(repeticoes," entrevistados \n")
        exit()
    else:
        print("valor invalido \n")
    print(repeticoes," entrevistados \n")
    time.sleep(2)