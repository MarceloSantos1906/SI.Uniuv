import numpy as np
import random
import time

class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.tempoi = []
    self.tempop = []
    self.tempopb = []
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
      print('Capacidade atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break
      if i == self.ultima_posicao:
        posicao = i + 1

    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    
    self.valores[posicao] = valor    
    self.ultima_posicao += 1

  def pesquisa_linear(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i
  
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao
    
    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      if self.valores[posicao_atual] == valor:
        return posicao_atual              
      elif limite_inferior > limite_superior:
        return -1
      else:
        if self.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual + 1
        else:
          limite_superior = posicao_atual - 1;

  def excluir(self, valor):
    posicao = self.pesquisa_binaria(valor)
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
          self.tempoi.append(tempof - tempo0)
      mediai = (sum(self.tempoi)/len(self.tempoi))

      for i in range(9999):
          tempo0 = time.time()
          vetor.pesquisa_linear(random.randint(0,9999))
          tempof = time.time()
          self.tempop.append(tempof - tempo0)
      mediap = sum(self.tempop)/len(self.tempop)

      for i in range(9999):
          tempo0 = time.time()
          vetor.pesquisa_binaria(random.randint(0,9999))
          tempof = time.time()
          self.tempopb.append(tempof - tempo0)
      mediapb = sum(self.tempopb)/len(self.tempopb)
      return mediai, mediap, mediapb

  def cinquenta(self):
      for i in range(49999):
          tempo0 = time.time()
          vetor.insere(random.randint(0,9999))
          tempof = time.time()
          self.tempoi.append(tempof - tempo0)
      mediai = (sum(self.tempoi)/len(self.tempoi))

      for i in range(49999):
          tempo0 = time.time()
          vetor.pesquisa_linear(random.randint(0,9999))
          tempof = time.time()
          self.tempop.append(tempof - tempo0)
      mediap = sum(self.tempop)/len(self.tempop)

      for i in range(49999):
          tempo0 = time.time()
          vetor.pesquisa_binaria(random.randint(0,9999))
          tempof = time.time()
          self.tempopb.append(tempof - tempo0)
      mediapb = sum(self.tempopb)/len(self.tempopb)
      return mediai, mediap, mediapb
  
  def cem(self):
      for i in range(99999):
          tempo0 = time.time()
          vetor.insere(random.randint(0,9999))
          tempof = time.time()
          self.tempoi.append(tempof - tempo0)
      mediai = (sum(self.tempoi)/len(self.tempoi))

      for i in range(99999):
          tempo0 = time.time()
          vetor.pesquisa_linear(random.randint(0,9999))
          tempof = time.time()
          self.tempop.append(tempof - tempo0)
      mediap = sum(self.tempop)/len(self.tempop)

      for i in range(99999):
          tempo0 = time.time()
          vetor.pesquisa_binaria(random.randint(0,9999))
          tempof = time.time()
          self.tempopb.append(tempof - tempo0)
      mediapb = sum(self.tempopb)/len(self.tempopb)
      return mediai, mediap, mediapb

#     CALCULAR TEMPO DE INSERÇÃO E PESQUISA
tempo_total = time.time()
media_rep_i = []
media_rep_p = []
media_rep_pb = []
print(f"10 000 valores:")
for i in range(1,4):
    print(f"{i}x 10 000 valores:")
    vetor = VetorOrdenado(10000)
    mediai, mediap, mediapb = vetor.dez()
    media_rep_i.append(mediai)
    media_rep_p.append(mediap)
    media_rep_pb.append(mediapb)
    print(f"Media para inserir: {mediai} s")
    print(f"Media para pesquisa linear: {mediap} s")
    print(f"Media para pesquisa binaria: {mediapb} s\n")
media_i = sum(media_rep_i)/len(media_rep_i)
media_p = sum(media_rep_p)/len(media_rep_p)
media_pb = sum(media_rep_pb)/len(media_rep_pb)
print(f"Media para inserir: {media_i} s")
print(f"Media para pesquisar linear: {media_p} s")
print(f"Media para pesquisa binaria: {mediapb} s\n")

media_rep_i = []
media_rep_p = []
media_rep_pb = []
print("50 000 valores:")
for i in range(1,4):
    print(f"{i}x 50 000 valores:")
    vetor = VetorOrdenado(50000)
    mediai, mediap, mediapb = vetor.cinquenta()
    media_rep_i.append(mediai)
    media_rep_p.append(mediap)
    media_rep_pb.append(mediapb)
    print(f"Media para inserir: {mediai} s")
    print(f"Media para pesquisa linear: {mediap} s")
    print(f"Media para pesquisa binaria: {mediapb} s\n")
media_i = sum(media_rep_i)/len(media_rep_i)
media_p = sum(media_rep_p)/len(media_rep_p)
media_pb = sum(media_rep_pb)/len(media_rep_pb)
print(f"Media para inserir: {media_i} s")
print(f"Media para pesquisar linear: {media_p} s")
print(f"Media para pesquisa binaria: {mediapb} s\n")

media_rep_i = []
media_rep_p = []
media_rep_pb = []
print("100 000 valores:")
for i in range(1,4):
    print(f"{i}x 100 000 valores:")
    vetor = VetorOrdenado(100000)
    mediai, mediap, mediapb = vetor.cem()
    media_rep_i.append(mediai)
    media_rep_p.append(mediap)
    media_rep_pb.append(mediapb)
    print(f"Media para inserir: {mediai} s")
    print(f"Media para pesquisa linear: {mediap} s")
    print(f"Media para pesquisa binaria: {mediapb} s\n")
media_i = sum(media_rep_i)/len(media_rep_i)
media_p = sum(media_rep_p)/len(media_rep_p)
media_pb = sum(media_rep_pb)/len(media_rep_pb)
print(f"Media para inserir: {media_i} s")
print(f"Media para pesquisar linear: {media_p} s")
print(f"Media para pesquisa binaria: {mediapb} s\n")
print(f"tempo total: {tempo_total}")


'''#        NÃO PERMITE INSERIR O MESMO NUMERO
vetor = VetorOrdenado(500)

while vetor.ultima_posicao < 499:
    num = random.randint(0,500)
    rep = vetor.pesquisa_binaria(num)
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
    pes = vetor.pesquisa_binaria(valor)
    if pes == -1:
        break
    else:
        vetor.excluir(valor)
vetor.imprime()'''