#Aula sobre FOR, em python o for funciona como um iterador
#for item in objeto
#   fazer algo

l = [1,2,3,4,5,6,7]
for i in l:
    print("Número: ", i)


print("Identificar se um número é par ou não")
for i in l:
    if(i%2 == 0):
        print("Par")
    else:
        print("Impar")

string = "O pelizza é um amigo!"
for t in string:
    print(t)

#característica especial sobre as tuplas
#tuple unpacking
tup = (1,2,3,4,5)
for t in tup:
    print(t)

tupla = [(1,2,3),(10,20,30)]
t1 = tupla[0]
print(t1)









