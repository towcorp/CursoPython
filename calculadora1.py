# função é tudo que retorna um valor
# metodo é tudo que não retorna
# definicão 'def' método

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
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subt (self):
        return self.a - self.b

    def multip (self):
        return self.a * self.b

    def divisao (self):
        return self.a / self.b


calculadora = Calculadora(10, 2)  # passsando os valores para a classe 

print(calculadora.a) # mostra o valor de 'a'

print(calculadora.soma())    # seleciona o parametro dentro da classe
print(calculadora.subt())
print(calculadora.multip())
print(calculadora.divisao())
