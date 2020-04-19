import pytest
import mock
from black_jack_game import Dealer
import black_jack_game

name_list = ['Dealer', 'Ishtiaq', 'Lars', 'Fredrik']
symbols = ['A', 'J', 'K', 'Q', 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
Note: player_bet was mocked when it was used to get player bet amount, however,
due to the use of get_bet (Player method), this is no more of any use.
'''
#@mock.patch.object(black_jack_game.Player, 'player_bet', side_effect=black_jack_game.player.mocked_get_each_player_bet)
def test_start_play():    
    dealer = Dealer(3)
    unique_cards = []
    assert len(dealer.deck_of_cards) == 52
    for i in range(4):
        for j in range(len(dealer.deck_of_cards) / 4):
            assert dealer.deck_of_cards[j].symbol == symbols[j]

    assert len(dealer.players) == 3

    dealer.start_play()
    assert len(dealer.deck_of_cards) == 52 - 3 * 2
    for card_1 in range (0, len(dealer.deck_of_cards) - 1):
        for card_2 in range(card_1 + 1, len(dealer.deck_of_cards) - 1):
            assert dealer.deck_of_cards[card_1].id != dealer.deck_of_cards[card_2 + 1].id

    for i in range(len(dealer.players)):
        assert dealer.players[i].name == name_list[i]
        assert dealer.each_player_bet[i] >= 100
        assert len(dealer.players[i].cards) == 2

        for j in range(len(dealer.players[i].cards)):
            for k in range(len(dealer.deck_of_cards)):
                assert (dealer.deck_of_cards[k].id) != dealer.players[i].cards[j].id

        



