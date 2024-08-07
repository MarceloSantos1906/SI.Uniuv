'''
Marcelo dos Santos Junior

Exercicio 4: 
Crie uma classe chamada Triangulo com os atributos lado1, lado2 e lado3. Em seguida, crie
um método chamado tipo que verifica se o triângulo é equilátero, isósceles ou escaleno. Crie
um objeto da classe Triangulo e execute o método tipo.

• Equilátero : possuem as três medidas iguais;
• Isósceles: São os polígonos que possuem duas medidas iguais e apenas uma diferente;
• Escaleno: são as figuras geométricas de três lados com as três medidas diferentes

'''
class triangulo:
    def tipo(lado1,lado2,base):
        if base == lado1 == lado2:
            print("Triangulo Equilátero")

        elif (lado1 == lado2 and lado2 != base) or (base == lado1 and base != lado2) or (base == lado2 and base != lado1):
            print("Triangulo Isóceles")

        elif (lado1 != lado2 and lado2 != base and lado1 != base) or (base != lado1 and base != lado2 and lado1 != lado2) or (base != lado2 and base != lado1 and lado1 != lado2):
            print("Triangulo Escaleno")

    lado1 = 0
    lado2 = 0
    base = 0
    tipo(lado1,lado2,base)