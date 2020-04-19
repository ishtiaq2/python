'''
Requirements:

Rules:
    1. Create representation of deck of cards
    2. Players: Computer Dealer and a Human Player
    3. 
Cards:
    Total: 52 cards
    Black:   2 - 10 (score)
    Red:     2 - 10 (score)
    A-Black: 2   1 or 11 if (A + A)score
    A-Red:   2   1 or 11 if (A + A) score
    Black:   J-Q-K  = 10 score, also known as faces cards
    Red:     J-Q-K  = 10 score, also known as faces cards


Game Actions:
    1. Create a deck of 52 cards
    2.  Randomly distribute 2 cards to Dealer and 2 cards to Player
        a. Player: 2 cards face up
        b. Dealer:   1 card face up, 1 card face down
    3.  Player can choose Hit or Stop
            Hit = ask for more card
            Stop = buzz for stop
    4.  If stop: count the value of cards on Player and Dealer side
            winner = the one closer to 21 or  (player is paid the same amount as he has a bet for)
                     if the player has an A and K as first cards (player is paid 150%)
                     if the player has a J and A as first cards (player is paid 150%)
            losser = the one abover 21
        else: continue from step 3. 
    Payouts:

        1.  If the player wins:
            The player is paid an equal amount that the player has bet on
            else if the player loses:
                loses all his bet money
            else:
                play another round


Total Value: 21
    Player: Getcloser to the total value than the dealer does.
'''


'''
Algorithm:
    Dealer Object:
        1. Create 52 Cards Object
        2. Register Players Object
        3. Calculate total Bet (Player1 Bet + P2 Bet +...)
        4. Distribute 2 Cards to each player on begin
            else 1 card. (each player calculate it's score)
        5. Observe action, for Hit or Stop, from each player
        6. Calculate Score of each player.
        7. Decide winner against Dealer.
        8. Distribute/collect bet
        9. Unregister Players who want to leave
        10. if there is player(s) continue from step 4.



    Card Object:
    13 x 4 set of cards object (A, 2 - 10, J, Q, K)
    Each having attributes:
        1. Value: 1 to 10
        2. Symbol: A, 1 to 10, J, Q, K
        3. 
    
    Player Object:
        Attributes:
            1. Name: 
            2. Bet
        Actions:
            1. Calculate your score
                if (score > 17):
                    stop:
                else: hit
            2. point out for stop or hit(false/true)
            2. add_bet on win(+bet)
            3. subs_bet on loss(-bet)


'''

import random
from black_jack_game import Dealer

dealer = Dealer(3)
dealer.start_play()

'''
for i in range(4):
    for j in range(13):
        print('id = {}'.format(i * 13 + j))
        #00 01 02 03 04 05 06 07 08 09 010 011 012 
        
'''

for card_1 in range (0, len(dealer.deck_of_cards) - 1):
        for card_2 in range(card_1 + 1, len(dealer.deck_of_cards) - 1):
            print ('card_1: {}, card_2: {}'.format(card_1, card_2))