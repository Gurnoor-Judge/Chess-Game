#GURNOOR JUDGE
#101162076

#defining the pieces to be used in the game
pieces=('K','k','Q','q','R','r','P','p','B','b','N','n','-')


'''this function checks the length of the input string by the user
@params  length_check(user_input)
@return length_check''' 
def length_check(user_input,i):
	while len(user_input) != 8:
		print("INVALID INPUT, PLEASE INPUT THE ROW AGAIN")
		user_input=input("Enter the Row "+str(i)+" of the chessboard: ")	
	
	
'''this function takes the input from the user and convert it to a 2-D list.
@params	input_function()
@return 2d list'''
def input_function():
	main_list=[]
	for i in range(1,9):
		main_list_2=[]
		user_input=input("Enter the Row "+str(i)+" of the chessboard: ")

		if user_input!=8:		
			length_check(user_input,str(i))
		if user_input not in pieces:
			letter_check(user_input,str(i))
		for j in range(8):
			main_list_2.append(user_input[j])
		main_list.append(main_list_2)
	#printing the 2d list
	for main_list_2 in main_list:
		for col in main_list_2:
			print(col,end='')
		print()

	
	return main_list
	
'''this function checks the letters input by the user, if there are letters other than given in the pieces variable it will show an error
@params letter_check(user_input,i)'''
def letter_check(user_input,i):
	list1=[]
	for x in range(8):
		if user_input[x] in pieces:
			list1.append(user_input[x])
		
	if len(list1)==8:
		return list1
	else:
		print("INVALID INPUT, PLEASE INPUT THE AGAIN")
		user_input=input("Enter the row "+str(i)+" of the chessboard: ")
		list2=list(length_check(user_input,i))
		return list2

	
'''this function add the values of white and black pieces and call out the win function
@params interpret_the_winner(main_list_2)'''
def interpret_the_winner(main_list_2):
	row=8
	column=8
	white=0
	black=0
	for m in range(0,row):
		for j in range(0,column):
			if  main_list_2[m][j]== 'K':
				white += 0
			elif main_list_2[m][j] == 'k':
				white += 0
			elif main_list_2[m][j] == 'Q':
				white += 10
			elif main_list_2[m][j] == 'q':
				white += 10
			elif main_list_2[m][j] == 'R':
				white += 5
			elif main_list_2[m][j] == 'r':
				black += 5
			elif main_list_2[m][j] == 'N':
				black += 3.5
			elif main_list_2[m][j] == 'n':
				black += 3.5
			elif main_list_2[m][j] == 'B':
				black += 3
			elif main_list_2[m][j] == 'b':
				black += 3
			elif main_list_2[m][j] == 'P':
				black += 1
			elif main_list_2[m][j] == 'p':
				black += 1
			elif main_list_2[m][j] == '-':
				black += 0
			elif main_list_2[m][j] == '-':
				black += 0

	Winning_player(white,black)

'''this function print out the winner
@params  Winning_player(white,black)''' 
def Winning_player(white,black):
	print("\nTHE CURRENT VALUE FOR BLACK IS: ",black)
	print("THE CURRENT VALUE FOR WHITE IS: ",white)
	if white > black:
		print("WHITE WILL WIN THE GAME")
	elif white == black:
		print("DRAW GAME")
	else:
		print("BLACK WILL WIN THE GAME")


#this function change the piece which the user want to change.
def change_piece(main_list_2):
	print("Enter the position of piece which you want to change: ")
	while True:
		while True:
			row=int(input("Enter the number of row: "))
			if row<1 or row>8:
				print("INVALID INPUT, PLEASE ENTER A VALID POSITION")
			else:
				break
		while True:
			column=int(input("Enter the number of column: "))
			if column<0 or column>9:
				print("INVALID INPUT, PLEASE ENTER A VALID POSITION")
			else:
				break
		while True:
			if main_list_2[row-1][column-1]=='-':
				print("THESE COORDINATES HAS NO PIECE")
				break
			else:
				break
		break
	
#enter the position where you want to move the piece
	while True:
		row2=int(input("Enter the row where you want to move the piece: "))
		if row2<1 or row2>8:
			print("INVALID INPUT, PLEASE ENTER A VALID POSITION")
		else:
			break
	while True:
		column2=int(input("Enter the column where you want to move the piece: "))
		if column2<1 or column2>8:
			print("INVALID INPUT, PLEASE ENTER A VALID POSITION")
		else:
			break
	if row==row2 or column==column2:
		return(main_list_2)
	else:
		main_list_2[row][column] = main_list_2[row2-1][row2-1]
		main_list_2[row][column] = '-'
		print("The chessboard positions after moving the pieces will be:")
		for main_list_2 in main_list:
			for col in main_list_2:
				print(col,end='')
		print()
	

def main():
	while True:
		instructions=input("\nDo you want to read instructions for this code? ")
		if instructions=='yes'.upper().lower():
			print("\nThis code will take an input from the user in the form of a chessgame and will interpret that who's winning.The user is asked to input the position of pieces(King, Queen, Bishop....etc) at their specific positions.\nType the letter as given in capital to represent WHITE piece and in lowercase to represent BLACK piece. Each piece is going to have specific value as follows:\n  PIECE		      VALUE\nKing-K/k 		0\nQueen-Q/q		10\nRook-R/r		5\nKnight-N/n		3.5\nBishop-B/b		3\nPawn-P/p		1\n	(-) for blank space")
			break
		elif instructions=='no'.upper().lower():
			break
#here are all the functions called
	main_list=[]
	main_list_2=input_function()
	interpret_the_winner(main_list_2)

	
	#at last asking the user whether he wants to continue or quit.
	while True:
		print("You have 3 options to either quit, update or start a new game\nPress A to change the position\nPress B to start a new game\nPress C to quit")
		user_options=input("What is your choice? ")
		if user_options=='A'.upper().lower():
			change_piece(main_list_2)
			interpret_the_winner(main_list_2)
		if user_options=='B'.upper().lower():
			input_function()
			interpret_the_winner(main_list)
		if user_options=='C'.upper().lower():
			exit()
#calling the main function
main() 

	
