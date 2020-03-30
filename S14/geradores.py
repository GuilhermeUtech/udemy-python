#Iteradores e geradores
def gencubes(n):
    for num in range(n):
        yield num ** 3 #n se comporta como função normal, mas sim gerador

for x in gencubes(10):
    print(x)

def gencubes2(n): #equivalente a gencubes só que essa carrega os valores na memória
    lst = []
    for num in range(n):
        lst += [num**3]
        return lst

#Imagina fazendo calc com números mt grandes, a gencubes2 ia dar merda na memória pq carrega em memória, diferente do yield

def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
        

for num in genfib(10):
    print(num)

print(list(genfib(10)))

g = genfib(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#Iteráveis que não se carregam na memória


