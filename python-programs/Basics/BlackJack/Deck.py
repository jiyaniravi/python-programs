import random

from Global import globals
from Card import Card

class Dack():

    def __init__(self):
        self.deck = []
        for suit in globals.suits:
            for rank in globals.ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The Deck has : "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

test_dack = Dack()
print(test_dack)
