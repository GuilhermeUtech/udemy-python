#zip(): cria um iterador que agrega elementos de cada um dos iteráveis
x = [1,2,3]
y = [8,9,10]
print(list(zip(x,y)))

for i in zip(x,y):
    print(max(i))

#o zip limita o tamanho das listas por baixo

d1 = {'a1': 1, 'a2': 2}
d2 = {'a1': 3, 'a2': 4}
print(list(zip(d1,d2)))

#condensa dois iteraveis juntos


