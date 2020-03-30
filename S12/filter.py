#Aula sobre Filter()
#Método que permite filtrar elementos dentro de um iteravel
#baseado no retorno de uma função

lista = [4,12,19,21,22,33]
print(list(filter(lambda x: x % 2 == 0, lista)))

