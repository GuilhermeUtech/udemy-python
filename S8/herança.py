#Aula sobre herança

class Animal(object):
    def __init__(self):
        print("Animal criado. ")
    
    def quem_sou_eu(self):
        print("Eu sou um animal. ")
    def comer(self):
        print("Que delícia de comida, nhom nhom")
    
    
class Cachorro(Animal): #note o heraça no lugar do object
    def __init__(self):
        Animal.__init__(self)
        print("I'm a dog")
    
    def quem_sou_eu(self):
        print("Sou um doguinho")
    
    def latir(self):
        print("Auau")
    
shake = Cachorro()
shake.quem_sou_eu()
shake.latir()
shake.comer()



