'''
Marcelo dos Santos Junior

Exercicio 2: 
Crie uma classe chamada Veiculo com os atributos marca, modelo e ano. Crie um método
chamado mostrar_dados que imprime na tela todas as informações do veículo

'''
class veiculo:
    def mostrar_dados(marca,modelo,ano):
        print(f"Marca: {marca} \nModelo: {modelo}, \nAno: {ano}")
    marca = "asdfghjkl"
    modelo = "xcvbnm"
    ano = 2023
    mostrar_dados(marca,modelo,ano)