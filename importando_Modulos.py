from televisao import Televisao  #'from' nome_arquivo.py 'import' Nome_classe
from calculadora1 import Calculadora


if __name__ == '__main__':
    televisao = Televisao()
    print('Está ligada: {}'.format(televisao.ligada))

    televisao.power()
    print('Está ligada: {}'.format(televisao.ligada))

    calculadora = Calculadora(5, 10)

    print('Resultado: {}'.format(calculadora.soma()))