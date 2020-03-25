#Aula sobre erros e exceções: https://docs.python.org/3/library/exceptions.html
#try:
#   tenta fazer algo aqui
#   ...
#except ExceptionI:
#   se causar ExceptionI, roda isso.
#except ExceptionII:
#   se causar ExceptionII, roda isso

#try:
#   se código aqui
#finally:
#    sete bloco de código é sempre executado

try:
    file = open('texto.txt', 'w')
    file.write("Testando")
except IOError:
    print("Erro ao abrir o arquivo. ")
else:
    print("Não houve erro. ")


#note agora, vamos induzir um erro tentando ler mas com modo de abertura
#de arquivo no modo 'r'
try:
    file = open('texto2.txt', 'r')
    file.write("Testando")
except IOError:
    print("Erro ao abrir o arquivo. ")
else:
    print("Não houve erro. ")

#agora vai dar erro

#outro exemplo
try:
    f = open('textfile', 'w')
    f.write('Testando novamente')
finally:
    print("Sempre fare isso aqui no fim pq é finally")

