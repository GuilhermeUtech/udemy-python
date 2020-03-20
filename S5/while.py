#Aula sobre While
#while teste:
#    declaracao de codigo
#else:
#    declaracao final de cod

x = 1
y = 2

while x<10 and y==2:
    print("Valor de X: ", x)
    x = x+1
else:
    print("Fim do while")

#exemplo com break

var = 1
lista = []

while True:
    lista += [var]
    var += 1
    if var > 10:
        break

print(lista)

hehe = 0
ate = 5
while hehe < ate:
    hehe += 1
    if hehe % 2 == 1:
        continue
    if(hehe % 2 == 0):
        print(hehe, "é par")



