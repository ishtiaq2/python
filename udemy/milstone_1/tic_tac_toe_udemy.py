import sys


player1 = ''
player2  = ''
board = ['-'] * 10
board_dimension = 0
markers = []

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
    player1 = ''
    while not (player1 == 'X' or player1 == 'O'):
        player1 = raw_input ('Player 1, choose X or O: ').upper()
    board[0] = '#'
    markers.append(player1)
    return (player1)


def place_marker(position, mark_index):
    if board[position] != '-' and '-' not in board:
        return 4
    elif board[position] != '-' and '-' in board:
        return 5
    board[position] = markers[mark_index]
    return rearrange_board(board[1:10], mark_index)#win_check(board)

def space_in_board(board):
    return '-' in board

def start_play(player1_marker, board):
    player2_marker = 'X' if player1_marker == 'O' else 'O'
    markers.append(player2_marker)
    print ('Player 1 marker : {}, Player 2 marker: {}').format(player1_marker, player2_marker)
    print ('Player 1 will go first.')
    play = raw_input("Are you ready to play? Enter y or n: ")
    if play.upper() != 'Y':
        return 0
    switch_player = markers.index(player1_marker)
    markers.append(switch_player)
    markers.append(switch_player + 1)
    pos = 0
    while space_in_board(board):
        pos = int(raw_input('Player {} move: '.format(switch_player + 1)))
        result = place_marker(pos, switch_player)
        display_board(board)
        if result == 1 or result == 2:
            game_ends(result)
            break
        elif result == 4:
            break
        elif result == 5:
            continue
        switch_player = 1 if switch_player == 0 else 0
    game_ends(3)

def game_ends(winner):
    if winner == 1 or winner == 2:
        print('Player {} wins! '.format(winner))   # ['O', 'X']
    else:
        print('Draw!')


def decide_winner(rearranged_board):
    global board_dimension
    if board_dimension >= len(rearranged_board):
        board_dimension = 0
        return 3
    else:
        if not markers[1] in rearranged_board[board_dimension] and \
            not '-' in rearranged_board[board_dimension] and \
            markers[0] in rearranged_board[board_dimension]:
            return 1
        elif not markers[0] in rearranged_board[board_dimension] and \
            not '-' in rearranged_board[board_dimension] and \
            markers[1] in rearranged_board[board_dimension]:
            return 2
        board_dimension += 1
        return decide_winner(rearranged_board)


def rearrange_board(board, mark_index):
    rearranged_board = []
    temp_board1 = []
    i = 0
    k = 0
    n = 0
    m = 0
    o = 0
    dim_0 = []
    dim_1 = []
    dim_2 = []
    dim_3 = []    
    
    for i in range (3):
        dim_0 = []
        dim_3 = []    
        n = 0
        for j in range(3):
            dim_0.append(board[j + k])          # 0, 1, 2       3, 4, 5     6, 7, 8
            dim_3.append(board[j + k + n - m ]) # 0, 3, 6       1, 4, 7     2, 5, 8
            n += 3                              # 0, 3, 6       0, 3, 6     0, 3, 6
            m += 1                              # 0, 1, 2       2, 3, 4     4, 5, 6
        rearranged_board.append(dim_0)    
        rearranged_board.append(dim_3)    
        dim_2.append(board[k + o])              #       0             4           8      
        dim_1.append(dim_3[j - o])
        o += 1                                  # 0                   1           2
        k += 3                                  # 0,            
        m = m - 1
    rearranged_board.append(dim_1)    
    rearranged_board.append(dim_2)        
    return decide_winner(rearranged_board)


player1_marker = assign_symbols()
display_board(board)
start_play(player1_marker, board)


# version 1.0