#aula sobre listas

my_list = [1,2,3]
print(my_list)

lista = [1, "abacate", 1.99, 'morango']
print(lista)
#pode por qualquer tipo dentro e seu tamanho n é preciso informar

#listas possuem vários métodos
lista.append(2020)
print(lista)

lista.reverse()
print(lista)

#acessando dados na lista
print(lista[3])

#da pra usar os :
print(lista[:3])

#concatenação de listas
nova_lista = my_list + lista
print(nova_lista)

#multiplicação
#print(lista * 10)

#tamanho da lista
print(len(lista))

#conte quantos abacates tem na lista
print(lista.count("abacate"))

#pop por padrao tira o ultimo da lista, mas posso passar a referencia do indice que eu quero tirar
lista.pop()
print(lista)

#lista de listas
lista_1 = ["guilherme", 21, "ciencia da computação"]
lista_2 = ["jessica", 20, "eng produção"]
lista_3 = ["fulano", 18, "quimica"]
lista_alunos = [lista_1, lista_2, lista_3]
print(lista_alunos)
print(len(lista_alunos)) #3

#acessando elementos em listas de listas
print(lista_alunos[1][1]) #virou uma matriz

#pegando só os nomes
first_col = [row[0] for row in lista_alunos]
print(first_col)
#pegando só os nomes
first_col = [row[0] for row in lista_alunos]
print(first_col)

#pegando só as idades
second_col = [row[1] for row in lista_alunos]
print(second_col)














