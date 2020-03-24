#Jogo da velha simples, sem um monte de coisa chata que poderia deixar mais bonito ou mais funcional.

campo = {"a1" : ' ', "a2" : ' ', "a3":' ', 
         "b1" : ' ', "b2" : ' ', "b3":' ',
         "c1" : ' ', "c2" : ' ', "c3":' ', 
        }

def mostrar_campo():
    print("|",campo['a1'], "|", campo['a2'], "|", campo['a3'],"|")
    print("|",campo['b1'], "|", campo['b2'], "|", campo['b3'],"|")
    print("|",campo['c1'], "|", campo['c2'], "|", campo['c3'],"|")


def jogada():
    posicao = input("Digite a posição que você deseja ocupar: ")
    campo[posicao] = input("Digite se você é X ou 0: ")



def vencedor():
    #Vencedor linha
    if(campo['a1'] == campo['a2'] and campo['a2'] == campo['a3']):
        if(campo['a1'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['a1'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['a1'] == ' '):
            return False

    if(campo['b1'] == campo['b2'] and campo['b2'] == campo['b3']):
        if(campo['b1'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['b1'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['b1'] == ' '):
            return False

    if(campo['c1'] == campo['c2'] and campo['c2'] == campo['c3']):
        if(campo['c1'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['c1'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['c1'] == ' '):
            return False

    #vencedor coluna
    if(campo['a1'] == campo['b1'] and campo['b1'] == campo['c1']):
        if(campo['a1'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['a1'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['a1'] == ' '):
            return False

    if(campo['a2'] == campo['b2'] and campo['b2'] == campo['c2']):
        if(campo['a2'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['a2'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['a2'] == ' '):
            return False

    if(campo['a3'] == campo['b3'] and campo['b3'] == campo['c3']):
        if(campo['a3'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['a3'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['a3'] == ' '):
            return False

    #vencedor diagonal 
    if(campo['a1'] == campo['b2'] and campo['b2'] == campo['c3']):
        if(campo['a1'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['a1'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['a1'] == ' '):
            return False
    if(campo['c1'] == campo['b2'] and campo['b2'] == campo['a3']):
        if(campo['a1'] == 'X'):
            print("X é o vencedor!")
            return True
        if(campo['a1'] == '0'):
            print("0 é o vencedor!")
            return True
        if(campo['a1'] == ' '):
            return False
    

while(vencedor() ==  False):
    mostrar_campo()
    jogada()

mostrar_campo()







