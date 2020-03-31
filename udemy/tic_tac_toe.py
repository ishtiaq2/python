import sys

player1 = ''
player2 = ''
counter = 0

rows, cols = (3, 3)
array = [[' ' for i in range(cols)] for j in range(rows)]
print array[0][0]

def draw_board(array):
    print '\n'
    print '     |        |      '
    print ' ', array[0][0], ' |  ', array[0][1], '   | ', array[0][2], ' '
    print '     |        |      '
    print '-----------------------'
    print '     |        |      '
    print ' ', array[1][0], ' |  ', array[1][1], '   | ', array[1][2], ' '
    print '     |        |      '
    print '-----------------------'
    print '     |        |      '
    print ' ', array[2][0], ' |  ', array[2][1], '   | ', array[2][2], ' '
    print '     |        |      '
    print '\n'

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


def start_play():
    switch_player = True
    global array
    global counter 

    while counter < 9:
        if switch_player:
            x = int(raw_input('Player 1 move: '))
            array = process_move(x, switch_player)
            draw_board(array)
            switch_player = False
        else:
            o = int(raw_input('Player 2 move: '))
            array = process_move(o, switch_player)
            draw_board(array)
            switch_player = True

        counter = counter + 1    
        calculate_score(array)

    print 'game finished'


def calculate_score(array):
    p1_count = 0
    p2_count = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == 'x':
                p1_count = p1_count + 1
            elif array[i][j] == 'o':
                p2_count = p2_count + 1

    for i in range(len(array)):
        for j in range(len(array)):
            if array[j][i] == 'x':
                p1_count = p1_count + 1
            elif array[j][i] == 'o':
                p2_count = p2_count + 1
    

    print 'Player 1 Score: {}, Player 2 Score: {}'.format(p1_count, p2_count)
            


def process_move(pos, switch_player):
    global array

    if pos == 1:
        if switch_player:
            array[2][0] = 'x' 
        else:
            array[2][0] = 'o'
    elif pos == 2:
        if switch_player:
                array[2][1] = 'x' 
        else:
            array[2][1] = 'o'
    elif pos == 3:
        if switch_player:
                array[2][2] = 'x' 
        else:
            array[2][2] = 'o'
    
    if pos == 4:
        if switch_player:
            array[1][0] = 'x' 
        else:
            array[1][0] = 'o'
    elif pos == 5:
        if switch_player:
            array[1][1] = 'x' 
        else:
            array[1][1] = 'o'
    elif pos == 6:
        if switch_player:
                array[1][2] = 'x' 
        else:
            array[1][2] = 'o'
    if pos == 7:
        if switch_player:
            array[0][0] = 'x' 
        else:
            array[0][0] = 'o'
    elif pos == 8:
        if switch_player:
            array[0][1] = 'x' 
        else:
            array[0][1] = 'o'
    elif pos == 9:
        if switch_player:
            array[0][2] = 'x' 
        else:
            array[0][2] = 'o'
    
    return array





def main():
    
    if assign_symbols():
        draw_board(array)
        start_play()

    else:
        return 0

if __name__ == '__main__':
    sys.exit(main())
