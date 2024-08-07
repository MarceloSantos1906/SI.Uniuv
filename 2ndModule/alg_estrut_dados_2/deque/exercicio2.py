'''
Marcelo dos Santos junior

Exercicio 2:
Criar um programa que simule a fila de trabalhos de impressão em uma impressora. Cada
trabalho de impressão é representado por um objeto Trabalho Impressao, que contém as
seguintes informações:
• Nome do arquivo a ser impresso
• Número de cópias a serem impressas
• Prioridade do trabalho de impressão (opcional)
Obs. Quando a impressora realizar a impressão ela deve mostrar o nome do arquivo e
quantas cópias.
'''
import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.nome = np.zeros(self.capacidade, dtype=object)
        self.quantidade = np.zeros(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, nome_, quantidade_):
        if self.__fila_cheia():
            print("A fila está cheia")
            return -1

        if self.numero_elementos == 0:
            self.nome[self.numero_elementos] = nome_
            self.quantidade[self.numero_elementos] = quantidade_
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if quantidade_ > self.quantidade[x]:
                    self.nome[x + 1] = self.nome[x]
                    self.quantidade[x + 1] = self.quantidade[x]
                else:
                    break
                x -= 1
            self.nome[x + 1] = nome_
            self.quantidade[x + 1] = quantidade_
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila está vazia")
            return

        nome_ = self.nome[self.numero_elementos - 1]
        quantidade_ = self.quantidade[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return nome_, quantidade_

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.nome[self.numero_elementos - 1], self.quantidade[self.numero_elementos - 1]

fila = FilaPrioridade(4)

a = fila.enfileirar("file1",3)
a = fila.enfileirar("file2",1)
a = fila.enfileirar("file3",2)
a = fila.enfileirar("file4",10)
a,b = fila.primeiro()
c = fila.desenfileirar()
print(f"{a} impresso com {b} copia(s)")
