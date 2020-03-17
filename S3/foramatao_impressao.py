# Aula sobre formatação de impressão

print("Isso aqui é uma string")
a = "string"
print("Isso é uma %s" %(a)) #se liga na malemolência, %r tbm funciona-> %s usa str e %r usa retr

a = 123.1234

print("Pontos flutuantes %1.2f" %(a))
print("Pontos flutuantes %1.5f" %(a))

a1 = "string"
a2 = 123

print("String: %s e um inteiro %r" %(a1,a2))

print(a1.upper())

#dicionário
metodoFormatExemplo = "Laranja: {a}, Pamonha: {b}, duentes: {c}".format(a=1, b="eita", c=12.122)
print(metodoFormatExemplo)

#https://pyformat.info/