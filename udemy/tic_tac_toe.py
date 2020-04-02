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
            rearr_array = rearrange_array(array)
            calculate_score(rearr_array)
            draw_board(array)
            switch_player = False
        else:
            o = int(raw_input('Player 2 move: '))
            array = process_move(o, switch_player)
            rearr_array = rearrange_array(array)
            calculate_score(rearr_array)
            draw_board(array)
            switch_player = True

        counter = counter + 1    
        #p1_score, p2_score = calculate_score(array)

        #print 'Player 1 Score: {}, Player 2 Score: {}'.format(p1_score, p2_score)    

        #if p1_score == 3 or p2_score == 3:
         #   print ' Final Score: Player 1 Score: {}, Player 2 Score: {}'.format(p1_score, p2_score)
          #  break
    #print 'Player 1 Score: {}, Player 2 Score: {}'.format(p1_score, p2_score)    
    #print 'game finished'

def calculate_score(rearrange_array):
    #recursion till len of rearrange_array
    print rearrange_array

'''
def calculate_score(array):
    p1_score, p2_score = calc_hor(array)
    if p1_score == 3 or p2_score:
        return p1_score, p2_score
    p1_score, p2_score = calc_vert(array)
    if p1_score == 3 or p2_score:
        return p1_score, p2_score
    p1_score, p2_score = calc_cross_left(array)
    if p1_score == 3 or p2_score:
        return p1_score, p2_score    
    p1_score, p2_score = calc_cross_right(array)
    if p1_score == 3 or p2_score:
        return p1_score, p2_score    

    return p1_score, p2_score
            
def calc_hor(array):
    p1_count = 0
    p2_count = 0

    for i in range(len(array)):
        l, m, n, o, p, q = 0, 0, 0, 0, 0, 0
        for j in range(len(array)):
            if array[i][j] == 'x':
                if l == 0:
                    l = 1
                elif m == 0:
                    m = 1
                elif n == 0:
                    n = 1
                    p1_count = 3
                    break
            elif array[i][j] == 'o':
                if o == 0:
                    o = 1
                elif p == 0:
                    p = 1
                elif q == 0:
                    q = 1
                    p2_count = 3
                    break
    print l, m, n, o, p, q
    return p1_count, p2_count

def calc_vert(array):
    p1_count = 0
    p2_count = 0

    for i in range(len(array)):
        l, m, n, o, p, q = 0, 0, 0, 0, 0, 0
        for j in range(len(array)):
            if array[j][i] == 'x':
                if l == 0:
                    l = 1
                elif m == 0:
                    m = 1
                elif n == 0:
                    n = 1
                    p1_count = 3
                    break
            elif array[j][i] == 'o':
                if o == 0:
                    o = 1
                elif p == 0:
                    p = 1
                elif q == 0:
                    q = 1
                    p2_count = 3
                    break
    print l, m, n, o, p, q
    return p1_count, p2_count
    

def calc_cross_left(array):
    p1_count = 0
    p2_count = 0

    
    l, m, n, o, p, q = 0, 0, 0, 0, 0, 0
    for j in range(len(array)):
        if array[j][j] == 'x':
            if l == 0:
                l = 1
            elif m == 0:
                m = 1
            elif n == 0:
                n = 1
                p1_count = 3
                break
        elif array[j][j] == 'o':
            if o == 0:
                o = 1
            elif p == 0:
                p = 1
            elif q == 0:
                q = 1
                p2_count = 3
                break
    print l, m, n, o, p, q
    return p1_count, p2_count

def calc_cross_right(array):
    p1_count = 0
    p2_count = 0

    
    l, m, n, o, p, q = 0, 0, 0, 0, 0, 0
    for j in range(len(array)):
        if array[j][len(array) - 1 - j] == 'x':
            if l == 0:
                l = 1
            elif m == 0:
                m = 1
            elif n == 0:
                n = 1
                p1_count = 3
                break
        if array[j][len(array) - 1 - j] == 'o':
            if o == 0:
                o = 1
            elif p == 0:
                p = 1
            elif q == 0:
                q = 1
                p2_count = 3
                break
    print l, m, n, o, p, q
    return p1_count, p2_count
'''    

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
