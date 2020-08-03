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

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')  # ler arquivo 'r' = read - modo de leitura
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') # split quebra o texto pelo crioterio informado '\n' = linhas
    #print(aluno_nota)

    lista_media = []


    for x in aluno_nota:
        lista_notas = x.split(',') # quebra a linha pela ',' = virgula
        #print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4     # coverte para inteiro e ja calcula a media
        print('Média: {}'.format(media(lista_notas)))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil    #importar biblioteca
    shutil.copy(nome_arquivo, '/home/cleiton/Documentos/') #caminho para salvar a copia // pode colocar o nome que quiser para salvar apos a barra do camino 

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/cleiton/Documentos/') # move o arquivo para o local determinado

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    #media_notas('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira_linha.\n')
    
    #aluno = 'Cesar,7,9,3,8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('text.txt')  # entre aspas o nome do arquivo que quer ler
