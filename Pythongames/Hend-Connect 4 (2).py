from random import randint
import os

COLS = 7 #The colunms for the board 
ROWS = 6 #The rows for the board 
Game_board = [[' ' for c in range(COLS)] for r in range(ROWS)]#This creates the board with dimension rows*cols and places empty spaces in the board 
letters=['A','B','C','D','E','F','G','H','I','J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
player= 2  #The number of players 
symbol=['X','O','V','H','M'] #The diff checker for each player 


#Function that creates the board 
def create_print_board(board): 
    for col in range(COLS):
        print("   "+letters[col], end="") 
    print("\n +" + "---+" * COLS)
    for row in range(ROWS):
        print(' |', end=" ")
        for col in range(COLS):
            print(board[row][col] + ' | ', end="")
        print("\n +"+"---+"*COLS)


# Function to get the player's input and validate it
def player_input(board,player):
    column=[]
    collist=[]
    # Define column list that has the acceptable range for each depending on the number of columns   
    for c in range(COLS):
        column.append(letters[c])


    # Get the player's input
    col=input("Player {}: Please input location eg. A,B,etc.: ".format(player+1))
    

    # Checks if the input is empty  
    while not col: 
        col=input("Player {}: Please input a vaild location: ".format(player+1))
  
    # Checks if the user input is whithin the accpetable range of columns
    while col not in column:
        col=input("Player {}: Please input a vaild location: ".format(player+1))

    # If the column is full then pass the turn
    if board[0][letters.index(col)]!=' ':
        print('This column is full, your turn is passed to the next player')
        col='pass'
          
    return col



# Function to run the game and check for win and draw.
def game(board):
    
    #print initial board
    print('Welcome to Connect 4 Game \n')
    create_print_board(board)
    
    #select players order randomly
    plist=list(range(player))
    order=[]
    for p in range(player):
        userind=randint(0,len(plist)-1)
        user=plist[userind]
        order.append(user)
        plist.remove(user)

        
    draw=False
    connect=False
    while (not connect) and (not draw) :
        for p in order:
            # Get players input
            col=player_input(board,p)

            #If the column is not full add checker to board
            if col!='pass':
        
                #Get the empty row in a column
                for row in range(ROWS):
                    if board[row][letters.index(col)]==' ':
                        r=row


                #Add the checker to the board    
                board[r][letters.index(col)]=symbol[p]
                create_print_board(board)
                

                #Check horizontal for connect 4
                for c in range(COLS-3):
                    for r in range (ROWS) :
                        if board[r][c]==symbol[p]and board[r][c+1]==symbol[p] and board[r][c+2]==symbol[p] and board[r][c+3]==symbol[p] :
                            connect=True

               
                # Check vertical for connect 4
                rows=list(range(3,ROWS))
                rows.reverse()
                for c in range (COLS):
                    for r in rows:
                        if board[r][c]==symbol[p] and board[r-1][c]==symbol[p] and board[r-2][c]==symbol[p]  and board[r-3][c]==symbol[p] :
                             connect=True
                                
                 # Check positive slope diaganols for connect 4
                for c in range(COLS-3):
                    for r in rows:
                        if board[r][c]==symbol[p] and board[r-1][c+1]==symbol[p]  and board[r-2][c+2]==symbol[p] and board[r-3][c+3]==symbol[p]:
                          connect=True
                      
                # Check negative slope diaganols for connect 4
                for c in range(3,COLS):
                     for r in rows:
                         if board[r][c]==symbol[p] and board[r-1][c-1]==symbol[p] and board[r-2][c-2]==symbol[p] and board[r-3][c-3]==symbol[p]:
                           connect=True
                # If Connect 4 then the player won and end the game
                if connect:
                    print('Player {} wins the game'.format(p+1))
                    break


                # If draw no one won and end the game
                draw=True
                for c in range(COLS):
                    for r in range(ROWS):
                         if board[r][c]==' ':
                             draw=False

                if draw==True and connect==False:
                    print('It is a draw')
                    break
                                     
game(Game_board)    


    
