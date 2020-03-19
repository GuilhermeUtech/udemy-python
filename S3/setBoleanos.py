#aula sobre conjuntos e booleanos
#é um conjunto de dados, e só permite valores únicos

x = set()
print(type(x))
x.add(10)
print(x)

#qual a utilidade disso? n sei

x.add(20)
print(x)

x.add(10)
print(x)
#agora eu entendi, eu só posso add valores únicos e ignora valores duplicados

#exemplo dahora, vai retornar apenas os elementos unicamente e ordenados
a = [11, 11, 11, 22, 22, 3, 4, 1, 2, 2]
b = set(a)
print(b)

#tipo de dado booleano
#verdadeiros ou falsos
ae = True
be = False
#percebe que é palavra reservada



