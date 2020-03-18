#aula sobre tuplas
#formato alternativo de dados em python, parecido com listas
#tuplas são imutáveis
#unica diferença entre tuplas e listas
t = (1,2,3)
tupla = (t, 1.21, "abacate", {'idade' : 12}, 1.21, 1.21) #aceita vários tipos de dados
print(tupla)
print(type(tupla))

#puxando dados em tuplas, padrão sem esquemas
print(tupla[2])

#métodos legais
print(tupla.index(1.21))
print(tupla.count(1.21))

#uma vez construída a tupla, ela é imutável!!!

