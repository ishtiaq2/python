import random


class Player():
    
    def __init__(self, player_counter, name_list):
        self.name = name_list[player_counter]
        self.bet = random.randint(1, 5) * 100
        self.score = []
        self.cards = []

    
    def get_bet(self):
        return self.bet

    def set_cards(self, _cards):
        self.score = []
        try:
            if len(_cards) > 1:
                for card in _cards:
                    self.cards.append(card)
                    self.score.append(card.value)
        except AttributeError:
            self.cards.append(_cards)
            for card in self.cards:
                self.score.append(card.value)
        
            

    def get_score(self):
        return self.score

    def add_bet(self, amount):
        self.bet = self.bet + amount
        self.continue_play()
    
    def sub_bet(self, amount):
        self.bet = self.bet - amount
        self.continue_play()

    def get_signal(self):
        signal = ''
        while signal != 's'.upper() and signal != 'h'.upper():
            signal = raw_input('{}: Enter s to stop or h to hit: '.format(self.name))
            if signal.upper() == 'S' or  signal.upper() == 'H':
                break
        return signal

    def continue_play(self):
        continue_play = input('{}: Enter y to continue: '.format(self.name))
        if continue_play == 'y'.toUpper():
            self.bet = self.bet + random.randint(1, 5) * 100
        else:
            self.bet = 0
    

    
class Card():

    def __init__(self, value, symbol, color, identifier):
        self.value = value
        self.symbol = symbol
        self.color = color
        self.id = identifier


def mocked_get_each_player_bet():
    return random.randint(1, 5) * 100