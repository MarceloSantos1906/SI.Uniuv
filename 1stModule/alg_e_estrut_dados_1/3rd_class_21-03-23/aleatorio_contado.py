import random

repeticoes = int(input("insira o numero de repetições: "))
numero_aleatorio: 0
soma = 0

for i in range(0, repeticoes,+1):
    numero_aleatorio = random.randint(1,10)
    print(numero_aleatorio)
    soma += numero_aleatorio
print("a soma é ", soma)