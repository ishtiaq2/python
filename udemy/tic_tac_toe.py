import sys

player1 = ''
player2 = ''
switch = True

def draw_board():
    print '     |        |      '
    print '     |        |      '
    print '     |        |      '
    print '-----------------------'
    print '     |        |      '
    print '     |        |      '
    print '     |        |      '
    print '-----------------------'
    print '     |        |      '
    print '     |        |      '
    print '     |        |      '

def assign_symbols():
    player1 = raw_input('Player 1: Do you wan to be X or O? ')
    player2 = 'x' if player1 == 'o' else 'o'
    print ('Player 1 is: {} and Player 2 is: {}').format(player1, player2)
    print ('Player 1 will go first.')
    st = raw_input("Are you ready to play? Enter y or n.")
    if str(st) == "y":
        return True
    else:
        return False



def main():
    
    if assign_symbols():
        draw_board()
    else:
        return 0

if __name__ == '__main__':
    sys.exit(main())
