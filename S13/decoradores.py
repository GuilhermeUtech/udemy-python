#Decoradores - Funções que alteram o comportamento de 
#outras funções. 

#def hello(nome = 'Rodrigo'):
#    return 'Olá, ' +nome

#print(hello())

#boasvindas = hello #doidera
#print(boasvindas())

#Criação de funções dentro de funções
"""
def hello(nome = 'Rodrigo'):
    print('Olá, '+nome)

    def tudobem():
        print("Tudo bem?")

    def comovaivc():
        print("Como vc vai?")
    
    print(locals())
    if nome == 'Rodrigo':
        return tudobem
    else :
        return comovaivc
func = hello()   #existe como se retornar funções
func() #usando aq a função retornada
"""

#Passando funções como argumento

def hello():
    print("Hello!")

def outra(func):
    print("Outra função aqui dentro")
    func() 

outra(hello)

#explicação definitiva:
def novo_decorador(func):
    def funcao_interna():
        print("Código antes de executar a função.")
        func()
        print("Código dps de executar a funcao")
    return funcao_interna

def precisa_decorar():
    print("Essa função precisa de decorador")

novo_decorador(hello)()

precisa_decorar = novo_decorador(precisa_decorar)
precisa_decorar()

@novo_decorador
def precisa_decorar():
    print("Essa funcao precisa de decorar!")

precisa_decorar()
