#Aula sobre métodos avançados em listas

l = [1,2,3]

l.append(4)
print(l)
l.append("abacaxi")
print(l)

print("Abacaxi aparece:", l.count("abacaxi"),"vezes.")

l.append([1,2,3])
print(l)

l.extend([10,20,30]) #quebra a lista e insere um a um na lista
print(l)

l.insert(2,55)
print(l)

pop_ = l.pop()
print(l)

l.remove("abacaxi")
print(l)

l.reverse()
print(l)


