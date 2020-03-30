#Neste projeto você estará criando um jogo de cartas blackjack completo
#em Python.
#Aqui estão alguns requisitos:
#   Você precisa criar um jogo BlackJacj baseado em texto.
#   O jogo precisa ter um jogador versus um dealer automatizado.
#   O jogador pode esperar ou pedir mais cartas.
#   O jogador deve escolher o seu valor de apostas.
#   Você precisa acompanhar o dinheiro total dos jogadores.
#   Você precisa alertar o jogador de vitórias, perdas, etc...
#E o mais importante:
#   Você deve usar POO e classes.
 
import random

jogando = False
fichas = 100
bet = 1
suits = ('h','d','c','s')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K')
card_val = {'A': 1, '2':2, '3':3, '4': 4, '5': 5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

#Classe carta ---------------------------
class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit+self.rank

    def grab_suit(self):
        return self.suit
    
    def grab_rank(self):
        return self.rank
    
    def draw(self):
        print(self.suit+self.rank)
#----------------------------------------

#Classe mão -----------------------------
class hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False
    
    def __str__(self):
        hand_comp = ""
        for cards in self.cards:
            card_name = cards.__str__()
            hand_comp += " " + card_name
        
        return "The hard has {}".format(hand_comp) 
    def card_add(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True

        self.value += card_val[card.rank]
    def calc_value(self):
        if(self.ace == 'True' and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw (self, hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw() 
#----------------------------------------
#Classe deck-----------------------------
class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += " " + card.__str__()
        return "The deck has "+deck_comp

#----------------------------------------
def make_bet():
    global bet
    bet = 0
    print("Quantas fixas vc quer apostar? ")
    while bet == 0:
        bet_comp = raw_input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("Aposta inválida, vc é pobre. Tem apenas: "+str(chip_pool))
