#Crie um gerador que gere os quadrados de números de um até n
def gensquares(n):
    for num in range(n):
        yield num ** 2

for x in gensquares(10):
    print(x)
print('--------')
#Crie um gerador que produze n numeros aleatórios entre um número baixo e alto (entradas). usar random
import random
def rand_num(low, high, n):
    for num in range(n):
        yield random.randint(low, high)

for x in rand_num(1,10,12):
    print(x)
print('--------')

#Use a função iter() para converter a string abaixo
s = 'hello'
for i in iter(s):
    print("haha")
print('--------')

#explique um caso de uso para um gerador usando a declaração yield onde vcê não deseja usar a funcao normal
""" Usaria em uma função onde carregar na memória poderia extourar o limite do python"""

