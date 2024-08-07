import random
import numpy as np


class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.zeros(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia")
            return -1

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila já está vazia")
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

fila = FilaCircular(10)
a = fila.enfileirar(7)
a = fila.enfileirar(3)
a = fila.enfileirar(8)
a = fila.enfileirar(10)

a = fila.primeiro()
print(a)
a = fila.desenfileirar()
a = fila.primeiro()
print(a)
a = fila.valores
print(a)
a = fila.valores[fila.final],fila.valores[fila.inicio]
print(a)