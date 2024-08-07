'''
Marcelo dos Santos junior

Exercicio 4:
Criar um programa que simule a pilha de acesso a sites em um navegador. O usuário sempre
que quiser pode voltar para o site anterior. O programa deve permitir mostrar quantos sites
existem na pilha e mostrar as informações do último site (Nome e link).
'''
import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.sites = np.empty(self.capacidade, dtype=object)

    def pilha_vazia(self):
        return self.topo == -1

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def empilhar(self, site):
        if self.pilha_cheia():
            print("A pilha está cheia")
            return

        self.topo += 1
        self.sites[self.topo] = site

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia")
            return

        site = self.sites[self.topo]
        self.topo -= 1
        return site

    def ultimo_site(self):
        if self.pilha_vazia():
            return None
        return self.sites[self.topo]

    def quantidade_sites(self):
        return self.topo + 1


pilha = Pilha(4)

pilha.empilhar("Nome1, url1")
pilha.empilhar("Nome2, url2")
pilha.empilhar("Nome3, url3")
pilha.empilhar("Nome4, url4")

a = pilha.ultimo_site()
b = pilha.quantidade_sites()
print("ultimo site:", a)
print("quantidade de sites:", b)

a = pilha.desempilhar()
b = pilha.ultimo_site()
c = pilha.quantidade_sites()
print("site desempilhado:", a)
print("ultimo site:", b)
print("quantidade de sites:", c)

