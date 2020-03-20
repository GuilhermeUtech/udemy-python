#Aula sobre funções
#def -> definir função
# def nome_função(parâmetros)

def primeira_funcao():
    print("Hello mundo!")

primeira_funcao()

def segunda_funcao(a):
    #função que retorna se o parâmetro é par ou impar
    if(a % 2 == 0):
        print("Par")
    else:
        print("Ímpar")

segunda_funcao(10)
segunda_funcao(7)

def terceira_funcao(a,b,c):
    print("print dentro da função: ", a+b+c)
    return a+b+c

retorno = terceira_funcao(12,12,33)
print("Retorno: ", retorno)

def quarta_funcao(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("Não é primo!") 
            break
    else:
        print("Primo!")

quarta_funcao(4)
quarta_funcao(13)


            







    


