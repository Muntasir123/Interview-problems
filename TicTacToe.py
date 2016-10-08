'''
Develop an program that will play tic tac toe between two users
Check for ties win's, and print out the winner, should there exist one
Muntasir Alam
'''
board = []
for i in range(0,3):
    board.append([" "," "," "])   # Fill the board

def print_board():
    for i in range(0,3):
        print "| ",
        for k in range(0,3):
            print board[i][k],
        print "|\n"

print "The first player to start will be player one with X\n, the second player will be O\n"
player_one = "X"
player_two = "O"
current_player_name = "Player One"
current_player = player_one
filled_board = False


# An algorithm for to be extended to an N by N board
# The idea is to make a graph with some default wins
def check_win_col():
    winner = " "
    for i in range(0,3):
        winner = board[i][0]
        for k in range(0,2):
            if board[i][0] != board[i][k+1]:
                winner = " "
                break
        if winner != " ":
            break
        if winner == " ":
            winner = board[0][i]
            for k in range(0,2):
                if board[0][i] != board[k+1][i]:
                    winner = " "
                    break
            if winner != " ":
                break
        if winner == " ":
            winner = board[0][0] #left edge
            for k in range(0,2):
                if board[0][0] != board[k+1][k+1]:
                    winner = " "
                    break
            if winner != " ":
                break
        if winner == " ":
            winner = board[0][2]
            for k in range(0,2):
                if board[0][2] != board[1+k][1-k]:
                    winner = " "
                    break
            if winner != " ":
                break
    return winner.lower()


while(filled_board == False):
    get_row = int(raw_input("Please enter which row you would like to move to " + current_player))
    get_col = int(raw_input("Please enter the col you want to move to" + current_player))
    board[get_row][get_col] = current_player
    print_board()
    check_win_col()

    count = 0
    for i in range(0,3):
        for k in range(0,3):
            if board[i][k] != " ":
                count+=1
    if count == 9:
        filled_board = True
        print "This is a tie game! Sorry about that!"

    win = check_win_col()
    print check_win_col()
    
    if win == "x":
        print "X has won!!"
        break
    
    if win == "o":
        print "O has won!!"
        break
    
    if current_player == player_one:
        current_player = player_two
    else:
        current_player = player_one


            
                


