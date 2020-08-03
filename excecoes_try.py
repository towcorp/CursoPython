lista = [1, 10]


try:  
    arquivo = open('text.txt', 'r') 
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print('fechando arquivo ')
    
    #x = a


except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')
except ArithmeticError:
    print('Não é possivel realizar operacao aritimetica')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))

else:                                                     # se não ouver erros será executado
    print('executa quando não ocorre exceção')
finally:                                                  # tudo no finnaly será executado com erro ou não
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()
