from Global import globals
from CommonFuncs import *
from Deck import Deck
from Hand import Hand
from Chips import Chips


while True:
    print('Welcome to black jack !')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand, dealer_hand)

    while globals.playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_chips)
            break
        
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    print('\n Player total chips : {}'.format(player_chips.total))
    print('\n')
    new_game = input('Do you want to play game again ? Press y or n : ')
    if new_game[0].lower() == 'y':
        globals.playing = True
        continue
    else:
        print('Thanks for playing !')
        break
