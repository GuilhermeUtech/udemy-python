#teste sobre a sessão
def word_lengths(palavra): #retorne quantas letras tem que cada palavra da string
    return print(list(map(len, palavra.split())))

word_lengths("rteste et ea a ae agf ga ga ga ga ")

#Use o filter para retornar as palavras de uma lista de palavras
#que começa com uma letra específica


def filter_words(word_list, letter):
    print(list(filter(lambda x: x[0] == letter,word_list)))

l = ['cachorro', 'quente', 'com', 'cachaça', 'é', 'bom', 'cara']
filter_words(l, 'c')

#Problema 4: use zip e list para retornar uma lista do mesmo comprimento
#onde cada valor é as duas cadeias de caracteres concatenadas
#juntas, 

def concatenate(l1,l2,connector):
    return print([word1+connector+word2 for (word1,word2) in zip(l1,l2)])

concatenate(['A','B'], ['a', 'b'], '-')

#os outros são mt fáceis e n vou fazer

