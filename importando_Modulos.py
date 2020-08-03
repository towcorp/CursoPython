from televisao import Televisao  #'from' nome_arquivo.py 'import' Nome_classe
from calculadora1 import Calculadora
from contador_letras import contador_letras, test 

if __name__ == '__main__':
    televisao = Televisao()
    print('Está ligada: {}'.format(televisao.ligada))

    televisao.power()
    print('Está ligada: {}'.format(televisao.ligada))

    calculadora = Calculadora(5, 10)

    print('Resultado: {}'.format(calculadora.soma()))

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)

    print('Total de letras por palacras na lista: {}'.format(total_letras))

    print(test())   # chamando a classe test

