#Exercícios exceção:

#1. Manuseie a exceção lançada pelo código abaixo usando
#os blocos try e except

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Operação inválida. ")

#2. Manuseie a exceção gerada pelo código usando os blocos
#try e except. Em seguinda, use um bloco finally para imprimir 'All done'

x = 4
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Divisão por 0. ")

#3. Escreva uma função que solicite um número inteiro e imprima o quadrado
#dele. Use um loop while com um try, except e else para contabilizar as entradas
#incorretas.

def ask(num):
    return num**2

while True:
    try:
        n = int(input("Digita um inteiro ai. "))
        print(ask(n))
        break
    except :
        print("Deu merda")
        continue

