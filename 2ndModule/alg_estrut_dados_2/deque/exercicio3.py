'''
Marcelo dos Santos junior

Exercicio 3:
Você foi contratado para desenvolver um programa para gerenciar uma pilha de livros em
uma biblioteca. O programa deve permitir que os funcionários da biblioteca adicionem novos
livros à pilha, removam livros da pilha e mostrem o último livro adicionado à pilha(e suas
informações Título da obra, autor(a) e ano).
'''
import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.livro = np.empty(self.capacidade, dtype=object)

    def pilha_vazia(self):
        return self.topo == -1

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def empilhar(self, livro):
        if self.pilha_cheia():
            print("A pilha está cheia")
            return

        self.topo += 1
        self.livro[self.topo] = livro

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia")
            return

        livro = self.livro[self.topo]
        self.topo -= 1
        return livro

    def ultimo_livro(self):
        if self.pilha_vazia():
            return None
        return self.livro[self.topo]

pilha = Pilha(4)

pilha.empilhar("titulo1, autor1, ano1")
pilha.empilhar("titulo2, autor2, ano2")
pilha.empilhar("titulo3, autor3, ano3")
pilha.empilhar("titulo4, autor4, ano4")

a = pilha.ultimo_livro()
print("ultimo livro:", a)

a = pilha.desempilhar()
b = pilha.ultimo_livro()
print("livro desempilhado:", a)
print("ultimo livro:", b)

