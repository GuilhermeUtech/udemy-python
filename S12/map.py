#lambda
def fahrenheit(T):
    return (9/5)*T + 32
temp = [9,22,40,90,120]
for t in temp:
    print(fahrenheit(t))

#map() -> cara isso é show de bola: redução de tamanho de código = aplica uma função sobre algum iterável
#Essa função, em Python, serve para aplicarmos uma função a cada elemento de uma lista, retornando uma nova
# lista contendo os elementos resultantes da aplicação da função.
print(list(map(fahrenheit, temp))) 
print(list(map(lambda t:(9/5)*t+32,temp)))




