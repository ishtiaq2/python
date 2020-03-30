import sys

player1 = ''
player2 = ''


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
    print 'Player 1: Do you wan to be X or O? \n'
    player1 = sys.stdin.read(1)

    player2 = 'X' if player1 == 'O' else 'O'
    print 'Player 1 is: {} and Player 2 is: {}'.format(player1, player2)



def main():
    draw_board()
    assign_symbols()

if __name__ == '__main__':
    sys.exit(main())
