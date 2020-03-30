#converta 2014 para a representação binária e hexadecimal
a = 1024
print("Hexadecimal", hex(a), "binária", bin(a))

#arredonde 5.23222 para duas casas decimais
b = 5.23222
print(round(b,2))

#verifique se cada letra na sequência s é minúscula
s = "hello how are you Maru, are you feeling okay?"
for i in s:
    if i.isupper():
        print("Nem todas são minúsculas.")
        break

#quantas vezes a letra 'w' aparece na string abaixo?
s = "twywywtwywbwhsjhwuwshshwuwwwjdjdid"
print(s.count("w"))

#encontre os elementos no set1 que não estão no set2:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set(set1.difference(set2)))

#encontre todos os elementos que estão no conjunto
print(set(set1.union(set2)))

#crie o dicionário {0:0,1:1, 2:8, 3:27,4:64} usando compreensão.
dict = {
    x:x**3 for x in range(5)
}
print(dict)

#inverta a lista abaixo:
l = [1,2,3,4]
l.reverse()
print(l)

#classifique a lista abaixo
l = [3,4,2,5,1]
l.sort()
print(l)


        