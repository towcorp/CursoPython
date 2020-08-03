'''
# open('test', 'w') cria um arquivo de texto ('w' = write)

arquivo = open('test.txt', 'a') # expecifica .txt no arquivo criado ('a' = continua escrevendo sem subscrever)
arquivo.write('\nsegunda linha') # Escreve no aruqivo, ## ('w') se ja tem texto ele subscreve


arquivo.close()
arquivo = open('c:/Documentos/arquivo.txt', 'w') # pode colocar o caminho do arquivo que quer abrir

'''
def escrever_arquivo(texto):
    arquivo = open('text.txt', 'w') 

    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('text.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')  # ler arquivo 'r' = read - modo de leitura
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    #escrever_arquivo('Primeira_linha.\n')
    #atualizar_arquivo('Terceira linha.\n')
    ler_arquivo('text.txt')  # entre aspas o nome do arquivo que quer ler
    