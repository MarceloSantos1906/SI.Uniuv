import numpy as np
import random
import time

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.tempoi = []
        self.tempop = []
        
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=float)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1 
            self.valores[self.ultima_posicao] = valor 

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1
    
    def dez(self):
        for i in range(9999):
            tempo0 = time.time()
            vetor.insere(random.randint(0,9999))
            tempof = time.time()
            self.tempoi.append(tempof-tempo0)
        mediai = (sum(self.tempoi)/len(self.tempoi))
        for i in range(9999):
            tempo0 = time.time()
            vetor.pesquisar(random.randint(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediap = sum(self.tempop)/len(self.tempop)
        return mediai, mediap

    def cinquenta(self):
        for i in range(49999):
            tempo0 = time.time()
            vetor.insere(random.randint(0,9999))
            tempof = time.time()
            self.tempoi.append(tempof - tempo0)
        mediai = (sum(self.tempoi)/len(self.tempoi))

        for i in range(49999):
            tempo0 = time.time()
            vetor.pesquisar(random.randint(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediap = sum(self.tempop)/len(self.tempop)
        return mediai, mediap
    
    def cem(self):
        for i in range(99999):
            tempo0 = time.time()
            vetor.insere(random.randint(0,9999))
            tempof = time.time()
            self.tempoi.append(tempof - tempo0)
        mediai = (sum(self.tempoi)/len(self.tempoi))

        for i in range(99999):
            tempo0 = time.time()
            vetor.pesquisar(random.randint(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediap = sum(self.tempop)/len(self.tempop)
        return mediai, mediap

#     CALCULAR TEMPO DE INSERÇÃO E PESQUISA
tempo_total = time.time()
media_rep_i = []
media_rep_p = []
print(f"10 000 valores:")
for i in range(1,4):
    print(f"{i}x 10 000 valores:")
    vetor = VetorNaoOrdenado(10000)
    mediai, mediap = vetor.dez()
    media_rep_i.append(mediai)
    media_rep_p.append(mediap)
    print(f"Media para inserir: {mediai} s")
    print(f"Media para pesquisar: {mediap} s\n")
media_i = sum(media_rep_i)/len(media_rep_i)
media_p = sum(media_rep_p)/len(media_rep_p)
print(f"Media para inserir: {media_i} s")
print(f"Media para pesquisar: {media_p} s\n")

media_rep_i = []
media_rep_p = []
print("50 000 valores:")
for i in range(1,4):
    print(f"{i}x 50 000 valores:")
    vetor = VetorNaoOrdenado(50000)
    mediai, mediap = vetor.cinquenta()
    media_rep_i.append(mediai)
    media_rep_p.append(mediap)
    print(f"Media para inserir: {mediai} s")
    print(f"Media para pesquisar: {mediap} s\n")
media_i = sum(media_rep_i)/len(media_rep_i)
media_p = sum(media_rep_p)/len(media_rep_p)
print(f"Media para inserir: {media_i} s")
print(f"Media para pesquisar: {media_p} s\n")

media_rep_i = []
media_rep_p = []
print("100 000 valores:")
for i in range(1,4):
    print(f"{i}x 100 000 valores:")
    vetor = VetorNaoOrdenado(100000)
    mediai, mediap = vetor.cem()
    media_rep_i.append(mediai)
    media_rep_p.append(mediap)
    print(f"Media para inserir: {mediai} s")
    print(f"Media para pesquisar: {mediap} s\n")
media_i = sum(media_rep_i)/len(media_rep_i)
media_p = sum(media_rep_p)/len(media_rep_p)
print(f"Media para inserir: {media_i} s")
print(f"Media para pesquisar: {media_p} s\n")
print(f"tempo total: {tempo_total}")

'''#        NÃO PERMITE INSERIR O MESMO NUMERO
vetor = VetorNaoOrdenado(500)
while vetor.ultima_posicao < 499:
    num = random.randint(0,500)
    rep = vetor.pesquisar(num)
    if rep == -1:
        vetor.insere(num)
    else:
        print("valor ja esta na lista.")
vetor.imprime()'''

'''#        APAGA TODOS OS NUMEROS DEFINIDOS EM "VALOR" DA LISTA
while vetor.ultima_posicao < 499:
    vetor.insere(random.randint(0,499))
vetor.imprime()

valor = 2
print(f"\n exluir numero {valor}\n")
while True:
    pes = vetor.pesquisar(valor)
    if pes == -1:
        break
    else:
        vetor.excluir(valor)
vetor.imprime()'''