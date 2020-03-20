#Dado o raio, escreva uma função que
#calcule o volume de uma esferea
from math import pi
def volume(raio): return (4/3)*pi*raio*raio*raio

def ran_check(num, low, hight): return num<=hight and num>=low

#escreva uma função que receba uma string
#e calcule o número de letras maiúsculas
#e minúsculas

def calc_lower_upper(entrada):
    up = 0
    low = 0

    for x in entrada:
        if x.isupper():
            up += 1
        elif x.islower():
            low += 1

    print("Upper :", up )
    print("Lower :", low )

#Escreva uma função em python que recebe uma
#lista e retorne uma nova lista com elementos
#exclusivos da primeira lista

def unique_list(l):
    b=set(l)
    return b

#print(unique_list([1,1,2,2,3,3]))

def mult_num_lista(l):
    aux = 1
    for i in l:
        aux = aux * i
    return aux

#print(mult_num_lista([2,2,2]))

def pallindrome(string):
    a = string[::-1]
    b = string[:]

    return b == a

#print(pallindrome("ovo"))

def isPangrama(string):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string.lower()
    for i in string:
        alfabeto.remove(i)
    if len(alfabeto) == 0:
        print("Pandrama")
    else:
        print("~Pangrama")

isPangrama("abcdefghijklmnopqrstuvwxyz")
isPangrama("abcdefglmnopqrstuvwxyz")



