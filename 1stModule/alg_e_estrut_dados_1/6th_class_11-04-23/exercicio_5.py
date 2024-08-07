'''
Marcelo dos Santos Junior

Exercicio 5: 
Crie uma classe chamada Carro com os atributos marca, modelo, ano e velocidadeAtual. Crie
um método chamado mostrar_dados que imprime na tela todas as informações do carro.
Crie um método chamado acelerar que aumenta a velocidade do carro em 10 km/h e um
método chamado frear que diminui a velocidade do carro em 10 km/h, desde que a
velocidade atual seja maior ou igual a 10 km/h

'''
class carro:
    def mostrar_dados(marca,modelo,ano,velocidadeAtual):
        print(f"Marce: {marca}\nModelo: {modelo}\nAno: {ano}\n Velocidade Atual: {velocidadeAtual}km/h")
    def acelerar(velocidadeAtual):
        velocidadeAtual += 10
        return velocidadeAtual
    def frear(velocidadeAtual):
        velocidadeAtual -= 10
        return velocidadeAtual
    marca = "asdghjkl"
    modelo = "zxcvbnm"
    ano = 0
    velocidadeAtual = 0
    velocidadeAtual_ = 0
    while True:
        print("1. Acelerar \n2. Frear")
        opcao = input("Digite uma das opções: ")
        if opcao == "1":
            velocidadeAtual = acelerar(velocidadeAtual)
            mostrar_dados(marca,modelo,ano,velocidadeAtual)
        elif opcao == "2":
            if velocidadeAtual <= 0: print("Velocidade insuficiente \n")
            else:
                velocidadeAtual_ = velocidadeAtual
                velocidadeAtual = frear(velocidadeAtual)
                if velocidadeAtual < 0:
                    print("Velocidade insuficiente \n")
                    velocidadeAtual = velocidadeAtual_
                elif velocidadeAtual >= 0: mostrar_dados(marca,modelo,ano,velocidadeAtual)
        else: print("Opção invalida\n")