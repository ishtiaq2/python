import sys
import argparse
import random
import player
from player import Player, Card


class Dealer():

    def __init__(self, num_of_players=2):
        self.num_of_players = num_of_players
        self.deck_of_cards = []
        self.dealer_cards = []
        self.players = []
        self.name_list = ['Dealer', 'Ishtiaq', 'Lars', 'Fredrik']
        self.each_player_bet = []
        self.create_deck_of_cards(4)
        
        self.register_players(self.num_of_players + 1)
    
    def start_play(self):
        self.get_each_player_bet()
        self.distribute_cards()
        self.show_score()


    def create_deck_of_cards(self, number):
        symbols = ['A', 'J', 'K', 'Q', 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score =   [1,   10,  10,  10,  2, 3, 4, 5, 6, 7, 8, 9, 10]
        num_of_deck_sets = 4
        for i in range(num_of_deck_sets):
            for j in range (len(symbols)):
                if i < 2:
                    color = 'RED'
                else:
                    color = 'BLACK'
                card = Card(score[j], symbols[j], color, i * len(symbols) + j)
                self.deck_of_cards.append(card)
                    

    
    def register_players(self, number_of_players):
        for i in range(number_of_players):
            player = Player(i, self.name_list)
            self.players.append(player)


    def get_each_player_bet(self):
        for i in range(len(self.players)):
            self.each_player_bet.append(self.players[i].get_bet())


    def distribute_cards(self, player=None):
        if player == None:
            for i in range(len(self.players)):
                #print (self.players[i].name)
                cards = []
                for j in range(2):
                    c = random.randint(0, len(self.deck_of_cards) - 1)
                    cards.append(self.deck_of_cards[c])
                    self.deck_of_cards.pop(c)

                self.players[i].set_cards(cards)
        else:
            c = random.randint(0, len(self.deck_of_cards) - 1)
            player.set_cards(self.deck_of_cards[c])
            self.deck_of_cards.pop(c)

        
    def observe_player_action(self):
        pass

    def show_score(self):
        for player in self.players:
            for s in player.get_score():
                s = s + s
            print ('{} score: {} = '.format(player.name, player.get_score(), s))

        for player in self.players:
            signal = player.get_signal()
            if (signal.upper() != 'S'):
                self.distribute_cards(player)
        self.show_score()

                




    def decide_winner(self):
        pass

    def distribute_collect_bet(self):
        pass

    def unregister_player(self):
        '''
        if one or more player continue from distributing cards
        '''
        pass


def main():
    parser = argparse.ArgumentParser('Black jack game')
    parser.add_argument('-n', '--num', type=int, help='enter number of players')
    # parser.add_argument('-b', '--bet', help='amount of bet by each player')
    args = parser.parse_args()
    black_jack = Dealer(args.num)
    black_jack.start_play()

if __name__=='__main__':
    sys.exit(main())

    