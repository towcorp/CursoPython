conjunto1 = {1, 2, 3, 4, 4, 2, 5}   # não aceita duplicidade
#conjunto1.add(6)
conjunto1.discard(2)

# união de conjuntos

conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)

print("União: {}".format(conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2) # mostra apenas os que se repetem
print('Intersecção: {} '.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto1.difference(conjunto2)  #mostra todo conjunto1 que não contem no conjunto2 
conjunto_diferenca2 = conjunto2.difference(conjunto1)  #mostra todo conjunto2 que não contem no conjunto1 
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simetrica: {}'.format(conjunto_diff_simetrica))  #printa todo o conjunto menos os iguais



conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

#subconjunto
conjunto_subset = conjunto_a.issubset(conjunto_b) # verifica se o primeiro conjunto contem no segundo
print('A é um subconjunto de B: {} '.format(conjunto_subset))   #  returna True ou False 

conjunto_subset = conjunto_b.issubset(conjunto_a) # verifica se o primeiro conjunto contem no segundo
print('B é um subconjunto de A: {} '.format(conjunto_subset))    #  returna True ou False 

#superconjunto -- inversamente ao subconjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a) #Verifica se o primeiro conjunto é um super conjunto doa segundo
print('B é um superconjunto de A: {}'.format(conjunto_superset))  #  returna True ou False 



# Remover duplicidade
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)  # 'set' converte para um conjunto - conjunto automaticamente remove as duplicidades
print(conjunto_animais)
#converter o conjunto em lista 
lista_anlimais = list(conjunto_animais) # 'list' converte o conjunto em lista
print(lista_anlimais)




