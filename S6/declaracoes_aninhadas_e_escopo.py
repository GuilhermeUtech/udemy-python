#Declarações aninhadas e escopo
#Isso é o basicão, sobre variáveis globais e blablabla

name = "Guilherme Utech"
def greet():
    name = "Roberto"

    def hello():
        print("Hello",name)
    #n encontrou local ele procura a proxima var na hierarquia
    hello()
    
greet()
