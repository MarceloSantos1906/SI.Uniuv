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
        for i in range(10000):
            tempo0 = time.time()
            vetor.insere(random.uniform(0,9999))
            tempof = time.time()
            self.tempoi.append(tempof-tempo0)
        mediai = (sum(self.tempoi)/len(self.tempoi))
        for i in range(10000):
            tempo0 = time.time()
            vetor.pesquisar(random.uniform(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediap = sum(self.tempop)/len(self.tempop)
        return mediai, mediap

    def cinquenta(self):
        for i in range(50000):
            tempo0 = time.time()
            vetor.insere(random.uniform(0,9999))
            tempof = time.time()
            self.tempoi.append(tempof - tempo0)
        mediai = (sum(self.tempoi)/len(self.tempoi))

        for i in range(50000):
            tempo0 = time.time()
            vetor.pesquisar(random.uniform(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediap = sum(self.tempop)/len(self.tempop)
        return mediai, mediap
    
    def cem(self):
        for i in range(100000):
            tempo0 = time.time()
            vetor.insere(random.uniform(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediai = (sum(self.tempoi)/len(self.tempoi))

        for i in range(100000):
            tempo0 = time.time()
            vetor.pesquisar(random.uniform(0,9999))
            tempof = time.time()
            self.tempop.append(tempof - tempo0)
        mediap = sum(self.tempop)/len(self.tempop)
        return mediai, mediap

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

'''
print("10 000 valores:")
vetor = VetorNaoOrdenado(10000)

for i in range(3):
    vetor.insere(random.uniform(0,9999))

for i in range(3):
    vetor.pesquisar(random.uniform(0,9999))
'''