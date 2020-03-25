#Aula sobre classes

##
# class Sample(object): #python obriga a por o object aqui dentro
#   pass
#x = Sample()
#print(type(x))
# #

class Dog(object):
    cor = "" #posso definir atributos aqui e no __init__
    def __init__(self, raça, cor): #função de inicialização, o self é obrigatório
        self.raça = raça
        self.cor = cor

shake = Dog("cocker", "azul")
nina = Dog("só deus sabe", "amarelo")


print(type(shake))


