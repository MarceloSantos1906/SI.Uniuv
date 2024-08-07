import random

# To find next gap from current
def getNextGap(gap):
	# Shrink gap by Shrink factor
	gap = (gap * 10)//13
	if gap < 1:
		return 1
	return gap

# Function to sort arr[] using Comb Sort
def comb_sort(arr):
    n = len(arr)
    # Initialize gap
    gap = n
    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True
    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap !=1 or swapped == 1:
        # Find next gap
        gap = getNextGap(gap)
        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False
        # Compare all elements with current gap
        for i in range(0, n-gap):            
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True
    return arr

def criarListaOrdenada(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(i)
    return vetor
def criarListaOrdenadaReversa(tamanho):
    vetor = []
    for i in reversed(range(tamanho)):
        vetor.append(i)
    return vetor
def criarListaDesordenada(tamanho):
    vetor = []
    for i in reversed(range(tamanho)):
        vetor.append(i)
    random.shuffle(vetor)
    return vetor
def criarListaQuaseOrdenada(tamanho):
    vetor = criarListaOrdenada(tamanho)
    temp = vetor[0]
    vetor[0] = vetor[len(vetor)-1]
    vetor[len(vetor)-1] = temp
    return vetor

tamanhos = [100, 1000, 10000, 100000]

for tamanho in tamanhos:
    print(f"\n        [Tamanho da lista " + f"{tamanho:,}".format(1000000).replace(',','.') + "]")
    print(f"\nLista ordenada:")
    lista = criarListaOrdenada(tamanho)
    %timeit -r 1 -n 1 comb_sort2(lista.copy())
    print(f"\nLista ordenada reversa:")
    lista = criarListaOrdenadaReversa(tamanho)
    %timeit -r 1 -n 1 comb_sort2(lista.copy())
    print(f"\nLista desordenada:")
    lista = criarListaDesordenada(tamanho)
    %timeit -r 1 -n 1 comb_sort2(lista.copy())
    print(f"\nLista ordenada com maior numero na frente:")
    lista = criarListaQuaseOrdenada(tamanho)
    %timeit -r 1 -n 1 comb_sort2(lista.copy())

'''
tamanhos = [10, 50, 100, 1000, 10000]
for tamanho in tamanhos:
    print(f"\n        [Tamanho da lista " + f"{tamanho:,}".format(1000000).replace(',','.') + "]")
    print(f"\nLista ordenada:")
    lista = criarListaOrdenada(tamanho)
    t = timeit.timeit(lambda: comb_sort(lista.copy()), number=1)
    print(f"Execution time: {t:.6f} seconds")
    print(f"\nLista ordenada reversa:")
    lista = criarListaOrdenadaReversa(tamanho)
    t = timeit.timeit(lambda: comb_sort(lista.copy()), number=1)
    print(f"Execution time: {t:.6f} seconds")
    print(f"\nLista desordenada:")
    lista = criarListaDesordenada(tamanho)
    t = timeit.timeit(lambda: comb_sort(lista.copy()), number=1)
    print(f"Execution time: {t:.6f} seconds")
    print(f"\nLista ordenada com maior numero na frente:")
    lista = criarListaQuaseOrdenada(tamanho)
    t = timeit.timeit(lambda: comb_sort(lista.copy()), number=1)
    print(f"Execution time: {t:.6f} seconds")
'''