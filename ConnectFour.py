#	Connect Four Game
#	Written from scratch because girlfriend wanted to play and we didnt have internet to download it on our phones
#	Andrew Woodward
# 	October 2016

def play_game():
	print("Lets Play")
	board = []
	for x in range(6):
		board.append(["0"] * 6)
	
	print_board(board)
	
	moves = 0
	
	while True:
		player1_insert(board)
		if four1_check(board):
			print_board(board)
			print("\nPlayer 1 Wins!")
			break
		moves+=1
		if moves == 36:
			print("\nIt was a draw!")
			break
		print_board(board)
		player2_insert(board)
		if four2_check(board):
			print_board(board)
			print("\nPlayer 2 Wins!")
			break
		moves+=1
		if moves == 36:
			print("\nIt was a draw!")
			break
		print_board(board)
	


def player1_insert(board):
	while True:
		column = input("Player 1 enter column (1-6): ")
		if not (column == "6" or column == "5" or column == "4" or column == "3" or column == "2" or column == "1"):
			print("Invalid input")
		else:
			break
	column = int(column)
	i=6
	while i > 0:
		if board[i-1][column-1] == "0":
			board[i-1][column-1] = "a"
			break
		i-=1
	return


def player2_insert(board):
	while True:
		column = input("Player 2 enter column (1-6): ")
		if not (column == "6" or column == "5" or column == "4" or column == "3" or column == "2" or column == "1"):
			print("Invalid input")
		else:
			break
	column = int(column)
	i=6
	while i > 0:
		if board[i-1][column-1] == "0":
			board[i-1][column-1] = "b"
			break
		i-=1
	return


def four1_check(board):
	
	#check vertical spaces
	for i in range(3):
		for j in range(6):
			if board[i][j] == "a" and board[i+1][j] == "a" and board[i+2][j] == "a" and board[i+3][j] == "a":
				return True
				
	#check horizontal spaces
	for i in range(6):
		for j in range(3):
			if board[i][j] == "a" and board[i][j+1] == "a" and board[i][j+2] == "a" and board[i][j+3] == "a":
				return True
				
	#check \ diagonals
	for i in range(3):
		for j in range(3):
			if board[i][j] == "a" and board[i+1][j+1] == "a" and board[i+2][j+2] == "a" and board[i+3][j+3] == "a":
				return True
				
	#check / diagonals
	for i in range(3,6):
		for j in range(3):
			if board[i][j] == "a" and board[i-1][j+1] == "a" and board[i-2][j+2] == "a" and board[i-3][j+3] == "a":
				return True
	
	return False
	
def four2_check(board):
	
	#check vertical spaces
	for i in range(3):
		for j in range(6):
			if board[i][j] == "b" and board[i+1][j] == "b" and board[i+2][j] == "b" and board[i+3][j] == "b":
				return True
	
	#check horizontal spaces
	for i in range(6):
		for j in range(3):
			if board[i][j] == "b" and board[i][j+1] == "b" and board[i][j+2] == "b" and board[i][j+3] == "b":
				return True
				
	#check \ diagonals
	for i in range(3):
		for j in range(3):
			if board[i][j] == "b" and board[i+1][j+1] == "b" and board[i+2][j+2] == "b" and board[i+3][j+3] == "b":
				return True
				
	#check / diagonals
	for i in range(3,6):
		for j in range(3):
			if board[i][j] == "b" and board[i-1][j+1] == "b" and board[i-2][j+2] == "b" and board[i-3][j+3] == "b":
				return True
	
	return


def print_board(board):       
    print("")
    print("1 2 3 4 5 6")
    #for row in board:
    #    print(" ".join(row))
    for i in range(6):
    	for j in range(6):
    		if board[i][j] == "a":
    			print('\x1b[1;31m'+'a'+'\x1b[0m' + ' ', end='')
    		elif board[i][j] == "b":
    			print('\033[36m'+'b'+'\033[0m' + ' ', end='')
    		else:
    			print(board[i][j] + " ", end='')
    	print("")
    	



if __name__ == "__main__":
	play_game()