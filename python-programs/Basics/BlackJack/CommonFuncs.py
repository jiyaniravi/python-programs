from Global.globals import playing
from Chips import Chips
from Deck import Deck
from Hand import Hand

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips you like to bet ? '))
        except:
            print('Sorry please provide integer !')
        else:
            if chips.bet > chips.total:
                print('Sorry, you dont have enough chips ! You have {}'.format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x= input('Hit or Stand? Enter h or s : ')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Players stand dealrs turn')
            playing = False
        else:
            print('Sorry I did not understand input : Enter h or s : ')
            continue
        break

def player_busts(chips):
    print('Player Busted !')
    chips.lose_bet()

def player_wins(chips):
    print('Player Won !')
    chips.add_bet()

def dealer_busts(chips):
    print('Dealer Busted !')
    chips.lose_bet()

def dealer_wins(chips):
    print('Dealer Won !')
    chips.win_bet()

def push():
    print('Dealer and Player Tie ! PUSH !')

def show_some(player, dealer):
    print('Dealers Hand : ')
    print('One card hidden !')
    print(dealer.cards[1])
    print('\n')
    print('Players Hand :')
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print('Dealers Hand : ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players Hand :')
    for card in player.cards:
        print(card)
