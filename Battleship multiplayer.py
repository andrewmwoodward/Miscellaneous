#	Multiplayer BattleShip
#	Modified version of battleship assignment from CodeAcademys Python cousr
#	A.Woodward
#	January 2016


from random import randint    

board1 = []
board2 = []

for x in range(5):
    board1.append(["O"] * 5)
    board2.append(["O"] * 5)  
    
def print_board_1(board):       
    print ""
    print "Single Player"
    for row in board:
        print " ".join(row)

def print_board_2(board1,board2):       
    print ""
    print " Player 1"
    for row in board1:
        print " ".join(row)
    print "----------"
    print " Player 2"
    for row in board2:
        print " ".join(row)    
        
def random_row(board):                    #creates random row location
    return randint(0, len(board) - 1)

def random_col(board):                    #creates random col location
    return randint(0, len(board[0]) - 1)

print " "
print "Let's Play Battleship!"

while True:
	players = raw_input("How many players? (1 or 2): ")
	if players != "1" and players != "2":
		print "Invalid entry, try again"
	else:
		break


if players == "1":
	print_board_1(board1)
	
	ship_row = random_row(board1)
	ship_col = random_col(board1)
	
	for turn in range(4):
		print "Turn", turn + 1
		guess_row = int(raw_input("Guess Row: "))
		guess_col = int(raw_input("Guess Col: "))
		if (guess_row == ship_row) and (guess_col == ship_col):
			print "Congratulations! You sunk my battleship!"
			break
		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "Oops, that's not even in the ocean."
			elif(board1[guess_row][guess_col] == "X"):
				print "You guessed that one already."
			else:
				print "You missed my battleship!"
				board1[guess_row][guess_col] = "X"
        	print_board_1(board1)
        	if turn == 3:
        		print "Game Over"
        
if players == "2":
	print_board_2(board1,board2)
	
	while True:
		ship1_row = int(raw_input("Player 1, enter your ships row: "))
		ship1_col = int(raw_input("Enter your ships col: "))
		if (ship1_row < 0 or ship1_row > 4) or (ship1_col < 0 or ship1_col > 4):
			print "Invalid entry"
		else:
			break
	
	print (chr(27) +"[2J")
	
	while True:	
		ship2_row = int(raw_input("Player 2, enter your ships row: "))
		ship2_col = int(raw_input("Enter your ships col: "))
		if (ship2_row < 0 or ship2_row > 4) or (ship2_col < 0 or ship2_col > 4):
			print "Invalid entry"
		else:
			break
			
	print (chr(27) +"[2J")
	print_board_2(board1,board2)
	
	while True:
		
		guess_row_1 = int(raw_input("Player 1 guess row: "))
		guess_col_1 = int(raw_input("Guess col: "))
		
		if (guess_row_1 == ship2_row) and (guess_col_1 == ship2_col):
			print "Congratulations you sunk player 2's battle ship!"
			break
		else:
			if (guess_row_1 < 0 or guess_row_1 > 4) or (guess_col_1 < 0 or guess_col_1 > 4):
				print "Oops, that's not even in the ocean."
			elif(board2[guess_row_1][guess_col_1] == "X"):
				print "You guessed that one already."
			else:
				print "You missed player two's battleship!"
				board2[guess_row_1][guess_col_1] = "X"
				
		print_board_2(board1,board2)
		
		guess_row_2 = int(raw_input("Player 2 guess row: "))
		guess_col_2 = int(raw_input("Guess col: "))
		
		if (guess_row_2 == ship1_row) and (guess_col_2 == ship1_col):
			print "Congratulations you sunk player 1's battle ship!"
			break
		else:
			if (guess_row_2 < 0 or guess_row_2 > 4) or (guess_col_2 < 0 or guess_col_2 > 4):
				print "Oops, that's not even in the ocean."
			elif(board1[guess_row_2][guess_col_2] == "X"):
				print "You guessed that one already."
			else:
				print "You missed player two's battleship!"
				board1[guess_row_2][guess_col_2] = "X"
		print_board_2(board1,board2)
		
		
		
    	
        		
        		
        		
        		
        		
        		
        		
        		
        		
        		