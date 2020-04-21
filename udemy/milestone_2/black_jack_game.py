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
        self.final_list = []
        self.name_list = ['Ishtiaq', 'Lars', 'Fredrik', 'Dealer']
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
                self.deck_of_cards.append(Card(score[j], symbols[j], color, i * len(symbols) + j))
                
                    

    
    def register_players(self, number_of_players):
        for i in range(0, number_of_players):
            if i == number_of_players - 1:
                i = -1
            player = Player(i, self.name_list)
            self.players.append(player)
            if i == -1:
                break


    def get_each_player_bet(self):
        for i in range(len(self.players)):
            self.each_player_bet.append(self.players[i].get_bet())


    def distribute_cards(self, player=None):
        if player == None:
            for i in range(len(self.players)):
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
        len_pl = len(self.players)

        if len(self.final_list) > 0 and len_pl > 0:
            for i in range(0, len(self.final_list)):
                for p in self.players:
                    if self.final_list[i].name == p.name:
                        for j in range(len_pl):
                            if self.players[j].name == p.name:
                                self.players.pop(j)
                                len_pl = len_pl - 1
                                break
        
        continued = False
        for i in range (len(self.players)):
            player = self.players[i]
            score = player.get_score()
            s = 0
            for j in range(len(score)):
                s = s + score[j]
            print ('{} score: {} = {}'  \
                .format(player.name, player.get_score(), s))
            if s > 22:
                self.final_list.append(player)
                self.players.pop(i)
            if i == len(self.players) - 1:
                    break
    
        if len(self.players) > 0:
            print ('******************************* Round completed! *****************')
            continued = True
            for i in range (len(self.players)):
                player = self.players[i]
                signal = player.get_signal()
                if (signal.upper() != 'S'):
                    self.distribute_cards(player)
                else:
                    self.final_list.append(player)
        if continued:
            self.show_score()
        else:
            self.final_result()

                




    def final_result(self):
        dealer = None
        for i in range (len(self.final_list)):
            if self.final_list[i].name == 'Dealer':
                dealer = self.final_list[i]
                self.final_list.pop(i)
                break

        for player in self.final_list:
            f_score = player.get_final_score()
            if  f_score <= 22 and  f_score > dealer.get_final_score() or \
                dealer.get_final_score() > 22:
                print ('************************************************************')
                print '{} balance before play: {} '.format(player.name, player.get_bet())
                player.add_bet(player.get_bet())
                print ('{} balance after play: {}'.format(player.name, player.get_bet()))
                print ('************************************************************')
            
            elif f_score < dealer.get_final_score() <= 22:
                print ('************************************************************')
                print ('{} balance before play: {}'.format(player.name, player.get_bet()))
                player.sub_bet(player.get_bet())
                print ('{} balance after play: {}'.format(player.name, player.get_bet()))
                print ('************************************************************')
            else:
                print ('{} balance is: {}'.format(player.name, player.get_bet()))
        return 0
        

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

    