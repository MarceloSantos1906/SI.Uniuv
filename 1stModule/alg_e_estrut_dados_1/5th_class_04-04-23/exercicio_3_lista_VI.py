'''
Marcelo dos Santos Junior

Exercicio 3: Escreva uma função que recebe uma string como parâmetro e retorna a string invertida

'''
def something():
    texto = input("Digite um fraze ou palavra: ") [::-1]
    return texto
texto_invertido = something()
print(f"Voce digitou: {texto_invertido}")