#Aula sobre métodos


class Dog(object):
    cor = "" #posso definir atributos aqui e no __init__
    def __init__(self, raça, cor): #função de inicialização, o self é obrigatório
        self.raça = raça
        self.cor = cor

    def latir(self):
        print("AUAU!")

shake = Dog("cocker", "caramelo")
shake.latir()    

class Circulo(object):
    pi = 3.14

    def __init__(self, raio = 1): #se n passar nada usa o 1, se ela passar usa o valor que ela passou
        self.raio = raio

    def calc_area(self):
        return self.pi * self.raio ** 2
    
    def atualiza_raio(self, novo_raio):
        self.raio = novo_raio
    
    def obtem_raio(self):
        return self.raio

c = Circulo(20)
print(c.obtem_raio())
print(c.calc_area())




