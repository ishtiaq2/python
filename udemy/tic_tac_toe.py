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
    global player1, player2
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
    global player1, player2

    while counter < 9:
        if switch_player:
            p1 = int(raw_input('Player 1 move: '))
            array = process_move(p1, switch_player)
            rearr_array = rearrange_array(array)
            #calculate_score(rearr_array)
            draw_board(array)
            switch_player = False
        else:
            p2 = int(raw_input('Player 2 move: '))
            array = process_move(p2, switch_player)
            rearr_array = rearrange_array(array)
            # calculate_score(rearr_array)
            draw_board(array)
            switch_player = True

        counter = counter + 1    
        p1_score, p2_score = calculate_score(rearr_array)

        if p1_score == 3 or p2_score == 3:
            break
    print 'Player 1 Score: {}, Player 2 Score: {}'.format(p1_score, p2_score)    
    print 'game finished'

def calculate_score(rearrange_array):
    #recursion till len of rearrange_array
    player_1_score = 0
    player_2_score = 0

    player_1_moves = 0
    player_2_moves = 0

    for i in range (len(rearrange_array)):
        player_1_score = 0
        player_2_score = 0
        for j in range(len(rearrange_array[i])):
            if rearrange_array[i][j] == 'x':
                player_1_score += 1
    
            elif rearrange_array[i][j] == 'o':
                player_2_score += 1
                player_2_moves += 1
    
        if player_1_score == 3 or player_2_score == 3:
            return player_1_score, player_2_score
    
    print 'Player 1 Moves: {}, Player 2 Moves: {}'.format(player_1_score, player_2_score)        
    return player_1_score, player_2_score

def process_move(pos, switch_player):
    global array
    global player1, player2

    if pos == 1:
        if switch_player:
            array[2][0] = player1
        else:
            array[2][0] = player2
    elif pos == 2:
        if switch_player:
                array[2][1] = player1 
        else:
            array[2][1] = player2
    elif pos == 3:
        if switch_player:
                array[2][2] = player1 
        else:
            array[2][2] = player2
    
    if pos == 4:
        if switch_player:
            array[1][0] = player1
        else:
            array[1][0] = player2
    elif pos == 5:
        if switch_player:
            array[1][1] = player1
        else:
            array[1][1] = player1
    elif pos == 6:
        if switch_player:
                array[1][2] = player1 
        else:
            array[1][2] = player2
    if pos == 7:
        if switch_player:
            array[0][0] = player1
        else:
            array[0][0] = player2
    elif pos == 8:
        if switch_player:
            array[0][1] = player1
        else:
            array[0][1] = player2
    elif pos == 9:
        if switch_player:
            array[0][2] = player1
        else:
            array[0][2] = player2
    
    return array

def rearrange_array(array):
    rearranged_array = []
    temp_array1 = []
    for i in range (len(array)):
        for j in range(len(array)):
            temp_array = []
            for k in range(len(array)):
                if i == 0:
                    temp_array.append(array[j][k])
                elif i == 1:
                    temp_array.append(array[k][j])
                elif i == 2:
                    if k == j:
                        temp_array1.append(array[k][j])
            if i < 2:
                rearranged_array.append(temp_array)
            
    rearranged_array.append(temp_array1)
    rearranged_array.append([array[0][2], array[1][1], array[2][0]])
    return rearranged_array


def main():
    
    if assign_symbols():
        draw_board(array)
        start_play()

    else:
        return 0

if __name__ == '__main__':
    sys.exit(main())
