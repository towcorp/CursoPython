class Error(Exception):    # obrigatorio criar uma classe 'Error' mesmo sem parametro
    pass

class InputError (Error):  # criar um tipo de Classe de erro que recebe a classe 'Error'
    def __init__(self, message):
        self.message = message
        

while True:
    try:
        x = int(input('entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')    # raise força uma exceção e personalisa a mensagem
        elif x < 0:
            raise InputError('Nota não pode se menor que 0')
        break
    except ValueError:   
        print('Valor invalido, Deve-se digitar apenas numeros.')
    except InputError as ex:
        print(ex)


