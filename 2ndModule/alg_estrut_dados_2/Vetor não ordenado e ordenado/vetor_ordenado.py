import numpy as np
import random
import time

class VetorOrdenado:
  
  def __init__(self, capacidade):
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
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]
      
      self.ultima_posicao -= 1

#     #CALCULAR TEMPO DE INSERÇÃO E PESQUISA
print("10 000 valores:")
vetor = VetorOrdenado(10000)
tempo0 = 0
tempof = 0
tempoi = []
tempop = []
tempopb = []

for i in range(3):
  for i in range(10000):
    tempo0 = time.time()
    vetor.insere(random.uniform(0,9999))
    tempof = time.time()
    tempoi.append(tempof-tempo0)
mediai = (sum(tempoi)/len(tempoi))
print(f"Media para inserir: {mediai} s")

for i in range(3):
  for i in range(10000):
    tempo0 = time.time()
    vetor.pesquisa_linear(random.uniform(0,9999))
    tempof = time.time()
    tempop.append(tempof - tempo0)
mediap = sum(tempop)/len(tempop)
print(f"Media para pesquisa linear: {mediap} s")

for i in range(3):
  for i in range(10000):
    tempo0 = time.time()
    vetor.pesquisa_binaria(random.uniform(0,9999))
    tempof = time.time()
    tempopb.append(tempof - tempo0)
mediapb = sum(tempop)/len(tempop)
print(f"Media para pesquisa binaria: {mediapb} s\n")

print("50 000 valores:")
vetor = VetorOrdenado(50000)
tempo0 = 0
tempof = 0
tempoi = []
tempop = []
tempopb = []

for i in range(3):
  for i in range(50000):
    tempo0 = time.time()
    vetor.insere(random.uniform(0,9999))
    tempof = time.time()
    tempoi.append(tempof-tempo0)
mediai = (sum(tempoi)/len(tempoi))

for i in range(3):
  for i in range(50000):
    tempo0 = time.time()
    vetor.pesquisa_linear(random.uniform(0,9999))
    tempof = time.time()
    tempop.append(tempof - tempo0)
mediap = sum(tempop)/len(tempop)

for i in range(3):
  for i in range(50000):
    tempo0 = time.time()
    vetor.pesquisa_binaria(random.uniform(0,9999))
    tempof = time.time()
    tempopb.append(tempof - tempo0)
mediapb = sum(tempop)/len(tempop)

print(f"Media para inserir: {mediai} s")
print(f"Media para pesquisa linear: {mediap} s")
print(f"Media para pesquisa binaria: {mediapb} s\n")

print("100 000 valores:")
vetor = VetorOrdenado(100000)
tempo0 = 0
tempof = 0
tempoi = []
tempop = []
tempopb = []

for i in range(3):
  for i in range(100000):
    tempo0 = time.time()
    vetor.insere(random.uniform(0,9999))
    tempof = time.time()
    tempoi.append(tempof-tempo0)
mediai = (sum(tempoi)/len(tempoi))

for i in range(3):
  for i in range(100000):
    tempo0 = time.time()
    vetor.pesquisa_linear(random.uniform(0,9999))
    tempof = time.time()
    tempop.append(tempof - tempo0)
mediap = sum(tempop)/len(tempop)

for i in range(3):
  for i in range(100000):
    tempo0 = time.time()
    vetor.pesquisa_binaria(random.uniform(0,9999))
    tempof = time.time()
    tempopb.append(tempof - tempo0)
mediapb = sum(tempop)/len(tempop)

print(f"Media para inserir: {mediai} s")
print(f"Media para pesquisa linear: {mediap} s")
print(f"Media para pesquisa binaria: {mediapb} s\n")


