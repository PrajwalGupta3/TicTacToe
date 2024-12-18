from random import randrange                               #used when computer makes a move
import time
def print_board(board):                                    #print the board in neat format
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")
def human_move(board):                                      #validate and enter move made by user
    x=False
    while not x:                                             # till x is false
        move=input("Enter the position you want to place O at:")
        x=len(move)==1 and move>='1'and move<='9'
        if not x:
            print("enter valid position")
            continue
        move=int(move)-1                                         # to convert the move into position on the board
        row=move//3    
        col=move%3                                                #Eg: move=1; row=0;    col=1     first row, second column
        check=board[row][col]       
        x=check not in ['O','X']                                   # willl see if check is occupied by 'O' or'X' or not 
        if not x:
            print("position already occupied, choose new location")
            continue                                          
    board[row][col]='O'
def free_pos(board):                                              # required by computer to make move
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col]!='X' and board[row][col]!='O':      # to check if position free or not
                free.append((row,col))                        # append a tuple to the list 'free'
    return free
    
def comp_move(board):                                                   # computer's move
      free=free_pos(board)                                    # gets a list of tuples of free positions
      count=len(free)                                           
      if count>0:
            x=randrange(count)                                 # selects random index
            row,col=free[x]                                    #from 'free' select the tuple mentioned by 'x' and puts it as row and column
            board[row][col]='X'                                 #free is a list so free(x) is wrong
def victory_check1(board,sign):                         # to check for winner row wise
    if sign=='O':
        winner='user'
    if sign=='X':
        winner='computer'
    count1,count2,count3=0,0,0
    for col in range(3):
        if(board[0][col]==sign):
            count1+=1
        if count1==3:
            return winner
    for col in range(3):
        if(board[1][col]==sign):
            count2+=1
        if count2==3:
            return winner
    for col in range(3):
        if(board[2][col]== sign):
            count3+=1
        if count3==3:
            return winner
    return None
def victory_check2(board,sign):                     # to check for winner column wise            
    if sign=='O':
        winner='user'
    if sign=='X':
        winner='computer'
    count1,count2,count3=0,0,0
    for row in range(3):
        if(board[row][0]==sign):
            count1+=1
        if count1==3:
            return winner
    for row in range(3):
        if(board[row][1]==sign):
            count2+=1
        if count2==3:
            return winner
    for row in range(3):
        if(board[row][2]==sign):
            count3+=1
        if count3==3:
            return winner
    return None
def victory_check3(board,sign):                    # to check for winner column wise  
    if sign=='O':
        winner='user'
    if sign=='X':
        winner='computer'
    count1,count2=0,0
    if(board[0][0]==sign):
        count1+=1
    if(board[1][1]==sign):
        count1+=1
    if(board[2][2]==sign):
        count1+=1
    if count1==3:
        return winner
    if(board[0][2]==sign):
        count2+=1
    if(board[1][1]==sign):
        count2+=1
    if(board[2][0]==sign):
        count2+=1
    if count2==3:
        return winner
    return None


user=input('enter your name:')      
board=[
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]
board[1][1]='X'         
user_move=True
free=free_pos(board)
while len(free):
    print_board(board)
    if user_move:
        human_move(board)                                    # user's turn
        winner1=victory_check1(board,'O')                                               
        winner2=victory_check2(board,'O')                       #checking if user won or not
        winner3=victory_check3(board,'O')
    else:
        print('computer is thinking................')
        time.sleep(5)
        print("Computer's turn")
        comp_move(board)                                      #comp turn
        winner1=victory_check1(board,'X')
        winner2=victory_check2(board,'X')                       #checking if computer won or not
        winner3=victory_check3(board,'X')
    if(winner1!=None or winner2!=None or winner3!=None):
        break
    user_move= not user_move                                   #changes from human turn to comp turn and vice versa
    free=free_pos(board)
print_board(board)
if(winner1== 'user'or winner2== 'user' or winner3== 'user'):
    print(user,'won.Congratulations!')
elif(winner1== 'computer'or winner2== 'computer' or winner3== 'computer'):
    print('computer won.',user,'lost.Better luck next time')
else:
    print('Tie.There is no winner.')