#aula sobre expressões lambda

#def square(num):
#    return num ** 2
#


#posso por assim ainda
def quadrado(num): return num **2

print(quadrado(5))


square = lambda num: num ** 2
print(square(5))

parOuImpar = lambda num: num % 2 == 0
print(parOuImpar(10))
primeiroChar = lambda s: s[0]
print(primeiroChar("pelizza é um amigo"))







