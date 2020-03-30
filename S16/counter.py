#Módulo de coleções
#Counter permite contar elementos dentro de um iteravel
from collections import Counter
l = [2,3,2,2,1,2,3,2,1,2,3,2,1]
print(Counter(l)) #retorna um "dicionário" com valores únicos e o número de vezes que ele aparece
print(Counter("abacate"))
print(Counter("Quantas palavras aparecem dentro dessa frase?".split()))
c = Counter("Abacate Mamão Abacate Abacaxi Macaxeira".split())
print(c.most_common(1))

#Existem vários métodos do Counter(), atenção a isso para
#saber quando utilizar.
print(c.values())
print(c.items())