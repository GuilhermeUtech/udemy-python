#Aula sobre compreensão em listas

# exemplo: x = [1,2,3,4,...,30]

lista = []
for i in range(0,30):
    lista.append(i)

#print(lista)

# Agora um exemplo otimizado 
x2 = [j for j in range(0,20)]
print(x2)

x3 = [k*2 for k in range(0,20)]
print(x3)

#criação de listas de pares
xpares = [a for a in range(0,20) if a%2 == 0]
print(xpares)

lista = []
lista = [cu for cu in 'Pelizza é um amigo']
print(lista)

#Converão de temperaturas

celcius = [30, 32, 28, 18]
fahrenheit = [(temp*(9/5) + 32) for temp in celcius ]
print(fahrenheit)