'''
Marcelo dos Santos junior

Exercicio 1:
Criar um programa que simule um banco(Implementar uma fila circular). A fila deve ter as
seguintes funcionalidades:
• Adicionar um novo cliente ao final da fila.
• Remover o próximo cliente da fila.
• Verificar quantos clientes ainda estão na fila.
• Visualizar o nome da primeira pessoa da fila.
Obs. O cliente deve ser um objeto adicionado em outro objeto do tipo lista. O objeto do tipo
cliente deve conter nome e número da conta
'''
import random
import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.cliente = np.empty(self.capacidade, dtype=object)
        self.conta = np.zeros(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, cliente_nome, conta_num):
        if self.__fila_cheia():
            print("A fila está cheia")
            return -1

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final = (self.final + 1) % self.capacidade
        self.cliente[self.final] = cliente_nome
        self.conta[self.final] = conta_num
        self.numero_elementos += 1
        return True

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila já está vazia")
            return None, None

        temp_cliente = self.cliente[self.inicio]
        temp_conta = self.conta[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.numero_elementos -= 1
        return temp_cliente, temp_conta

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.cliente[self.inicio], self.conta[self.inicio]

    def tamanho_fila(self):
        if self.__fila_vazia():
            return -1
        return len(self.cliente)

fila = FilaCircular(10)
a = fila.enfileirar("something",8)
a = fila.enfileirar("that",6)
a = fila.enfileirar("yup",4)
a = fila.enfileirar("this",1)

a = fila.primeiro()
print(a)
a = fila.desenfileirar()
a = fila.primeiro()
print(a)
a = fila.cliente, fila.conta
print(a)
a = fila.cliente[fila.final],fila.conta[fila.final],fila.cliente[fila.inicio],fila.conta[fila.inicio]
print(a)
a = fila.tamanho_fila()
print(a)