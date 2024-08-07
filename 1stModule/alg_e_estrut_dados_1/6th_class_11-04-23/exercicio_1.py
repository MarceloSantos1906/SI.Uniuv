'''
Marcelo dos Santos Junior

Exercicio 1: 
Crie uma classe Pessoa com as seguintes propriedades: nome, idade e profissão. Em seguida,
crie um objeto da classe Pessoa e imprima suas propriedades

'''
class pessoa:
    def __init__(self) -> None:
        pass
    def propriedade(nome,idade,profissao):
        print(f"Nome: {nome} \nIdade: {idade} \nProfissão: {profissao}")
    nome = "Marcelo"
    idade = 23
    profissao = "Suporte tecnico"
    propriedade(nome,idade,profissao)