lista = []
genero = []
altura = []
alturaf = []
alturam = []
feminino = 0
masculino = 0
media = 0

for i in range (4):
    print("1.Feminino 2.Masculino")
    genero.append(input("Informe o genero: "))
    if genero[i] == "1":
        feminino += 1
        alturaf.append(float(input(f"Digite a altura: ")))
    elif genero[i] == "2":
        masculino += 1
        alturam.append(float(input(f"Digite a altura: ")))
    else: print("genero invalido")

maior = alturaf[0]
menor = alturaf[0]

for i in range(len(alturaf)):
    if alturaf[i] > maior:
        maior = alturaf[i]
    if alturaf[i] < menor:
        menor = alturaf[i]

for i in range(len(alturam)):
    if alturam[i] > maior:
        maior = alturam[i]
    if alturam[i] < menor:
        menor = alturam[i]

print(f"A maior altura é {maior}cm e a menor altura é {menor}cm")
media = (sum(alturaf))/(len(alturaf))
print(f"A media da altura das mulheres é {media}")
print(f"{masculino} Homens")