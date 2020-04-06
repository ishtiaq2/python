player1 = ''
player2  = ''

def display_board(board):
    print(' ' + ' | ' + ' ' + ' | ')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    #print(' ' + ' | ' + ' ' + ' | ')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print(' ' + ' | ' + ' ' + ' | ')
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ' + ' | ' + ' ' + ' | ')


def assign_symbols():
    
    global player1, player2
    while player1 != 'X' and player1 != 'O':
        player1 = raw_input ('Player 1, choose X or O: ').upper()

    player2 = 'X' if player1 == 'O' else 'O'
    return (player1, player2)
    
    #print ('Player 1 will go first.')
    #st = raw_input("Are you ready to play? Enter y or n.")


def start_play(player1_marker, player2_marker):
    board = [''] * 10
    print ('Player 1 marker : {}, Player 2 marker: {}').format(player1_marker, player2_marker)
    while continue_play(board):
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


def continue_play(board):
    pass

test_board = [ ' '] * 10
player1_marker, player2_marker = assign_symbols()
display_board(test_board)
#start_play(player1_marker, player1_marker)