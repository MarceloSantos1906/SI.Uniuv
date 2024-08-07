'''
Marcelo dos Santos junior

Exercicio 5:
Criar uma fila de banco com prioridade levando em consideração a idade do cliente. Porém
é importante criar uma regra, a cada 3 clientes com prioridade é necessário atender um sem
prioridade. Criar todas as funções necessárias para uma fila.
'''
import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia")
            return -1

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            if self.numero_elementos % 3 == 0:
                while x >= 0:
                    if valor > self.valores[x]:
                        self.valores[x + 1] = self.valores[x]
                    else:
                        break
                    x -= 1
            else:
                while x >= 0:
                    if valor >= self.valores[x]:
                        self.valores[x + 1] = self.valores[x]
                    else:
                        break
                    x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila está vazia")
            return

        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]

fila = FilaPrioridade(10)

a = fila.enfileirar(1)
a = fila.enfileirar(23)
a = fila.enfileirar(145)
a = fila.enfileirar(14)
a = fila.enfileirar(16)
a = fila.enfileirar(143)
a = fila.enfileirar(10)
a = fila.enfileirar(27)
a = fila.enfileirar(45)
a = fila.enfileirar(19)

a = fila.primeiro()
print(a)
a = fila.valores
print(a)
