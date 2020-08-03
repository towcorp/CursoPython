# função é tudo que retorna um valor
# metodo é tudo que não retorna
# definicão 'def'

def soma(a, b):
    return a + b

def subt (a, b):
    return a - b

def multip (a, b):
    return a * b

def divisao (a, b):
    return a / b

# transformar todos metodos 'def' em classes

# Class sempre comeca com maiuscula
class Calculadora:   
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subt (self, a, b):
        return a - b

    def multip (self, a, b):
        return a * b

    def divisao (self, a, b):
        return a / b


calculadora = Calculadora()  # passsando os valores para a classe 


if __name__ == '__main__':  # se for chamado pelo proprio aruquivo executa se não for não executa
    print(calculadora.soma(10, 2))    # seleciona o parametro dentro da classe e coloca os valores
    print(calculadora.subt(5, 3))
    print(calculadora.divisao(100, 2))
    print(calculadora.multip(10, 5))

