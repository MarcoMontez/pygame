import numpy as np

board = np.zeros((3,3))
board_p1_victory = np.array([[1,0,-1],[1,-1,0],[1,0,-1]]) 
board_p2_victory = np.array([[-1,-1,-1],[0,0,1],[1,0,1]])
board_p1_trace_win = np.array([[1,0,-1],[0,-1,0],[-1,0,1]])  
board_full = np.array([[1,1,-1],[-1,-1,1],[-1,1,0]])  

board = board

print(board,'\n')


def play_piece(x,y,player):
    """plays the piece on the board"""
    if board[x,y] != 0:
        print('That spot is already taken, choose another one!')
        return 'spot_already_taken'

    board[x,y] = 1 * player
    return 'piece_played'

def check_victory():
    """Checks if any player has won the game"""
    sum_cols = np.sum(board,axis=0)
    sum_rows = np.sum(board,axis=1)
    diagonal_1 = np.trace(board)
    diagonal_2 = np.trace(np.fliplr(board))

    if (max(sum_cols)==3 or max(sum_rows)==3 or diagonal_1 == 3 or diagonal_2 == 3):
        # print("Player 1 victory")
        return "p1_win"
    elif(min(sum_cols)==-3 or min (sum_rows)==-3) or diagonal_1 == -3 or diagonal_2 == -3:
        # print("Player 2 victory")
        return "p2_win"
    # print("No victory still")
    return "no_win"


def is_board_full():
    """Checks if board is full"""
    num_pieces = np.sum(np.abs(board))
    print("Number of pieces in board {}".format(num_pieces))
    if num_pieces == 9:
        return True
    return False

def player_play_message(player):
    player_dict = {1:'Player 1',-1:'Player 2'}
    player_name = player_dict[player]
    print("{} it's your turn to play!".format(player_name))
    return

def get_user_input():
    x, y = input("Enter your play coordinates: ").split()
    return x,y


player = 1


while (~is_board_full()) :
    if is_board_full():
        print("\nIts a draw!")

    player_play_message(player)
    print(board)
    x,y = get_user_input() # reload if user inputs wrong values
    # print('The values you inputed are', x,y)
    play_piece(int(x),int(y),player)
    
    play_result = check_victory() # On victory check if player wants to repeat
    if play_result == 'p1_win':
        print("\n\n\nPlayer 1 Victory!!!")
        break
    elif play_result =='p2_win':
        print("\n\n\nPlayer 2 Victory!!!")
        break

    player = -1 * player
