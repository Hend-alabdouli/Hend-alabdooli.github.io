# This code is a battleship game

# Import required libraries 
from random import randint
import os

# Define variable 
DIMENSION= 10  #size of board 
SHIP_SIZE = 4 #number of ships
#rows, cols = (DIMENSION, DIMENSION) 
Game_board = [['.' for c in range(DIMENSION)] for r in range(DIMENSION)] # Creates game board with size=dimesion*dimesion 
Cheat_board= [['.' for c in range(DIMENSION)] for r in range(DIMENSION)] # Creates a hidden board with size=dimesion*dimesion (show the ship location) 
letters=['A','B','C','D','E','F','G','H','I','J']

# This function creates and prints a board

def create_print_board(board): 
    for col in range(DIMENSION):
        print("   "+letters[col], end="") 
    print("\n +" + "---+" * DIMENSION)
    for row in range(DIMENSION):
        print(str(row) + '|', end=" ")
        for col in range(DIMENSION):
            print(board[row][col] + ' | ', end="")
        print("\n +"+"---+"*DIMENSION)

#This function places SHIP_SIZE number of consecutive ships randomly on the board    
def create_ship(board):
    # Define lists that will store the location of the ships 
    prev_shiprow=[]
    prev_shipcol=[]
    for ship in range(SHIP_SIZE):
        shiprow, shipcol= randint(0,DIMENSION-1),randint(0,DIMENSION-1) # Randomly select row and column location 
        if(ship==1): # For the second ship
            # Define a list that stores the possible locations of the second ship depending on the pervious ship 
            ship_locations=[[prev_shiprow[0]+1,prev_shipcol[0]],[prev_shiprow[0],prev_shipcol[0]+1],[prev_shiprow[0]-1,prev_shipcol[0]],[prev_shiprow[0],prev_shipcol[0]-1]]
             # This loop will keep on taking random row, col locations for ship 2 until they are within the accepted location list above
            while (shiprow in prev_shiprow and shipcol in prev_shipcol) or ([shiprow,shipcol] not in ship_locations):
                shiprow,shipcol= randint(0,DIMENSION-1),randint(0,DIMENSION-1)
        elif(ship>1):# For all ships >2
            rowdiff=prev_shiprow[ship-1]-prev_shiprow[ship-2] # To check if the ships are consecutive on the same row or column
            coldiff=prev_shipcol[ship-1]-prev_shipcol[ship-2] # To check if the ships are consecutive on the same row or column
            if rowdiff==0: # If ships are on the same row
                 # Define a list that stores the possible locations of the ship depending on the pervious ship 
                ship_locations=[[prev_shiprow[ship-1],prev_shipcol[ship-1]+1],[prev_shiprow[ship-1],prev_shipcol[ship-1]-1],[prev_shiprow[0],prev_shipcol[0]+1],[prev_shiprow[0],prev_shipcol[0]-1]]
            elif coldiff==0: # If ships are on the same column
                # Define a list that stores the possible locations of the ship depending on the pervious ship 
                ship_locations=[[prev_shiprow[ship-1]+1,prev_shipcol[ship-1]],[prev_shiprow[ship-1]-1,prev_shipcol[ship-1]],prev_shiprow[0]+1,prev_shipcol[0],[prev_shiprow[0]-1,prev_shipcol[0]]]
            # This loop will keep on taking random row, col locations for ship 2 until they are within the accepted location list above
            while (shiprow in prev_shiprow and shipcol in prev_shipcol) or ([shiprow,shipcol] not in ship_locations):
                shiprow, shipcol= randint(0,DIMENSION-1),randint(0,DIMENSION-1)
        # Appened location of ship to store in the list 
        prev_shiprow.append(shiprow)
        prev_shipcol.append(shipcol)
    for row in prev_shiprow:
        for col in prev_shipcol:
            board[row][col]='X' # Add location of the ships to the board 

# This function asks the users input for a ship location and makes sure there is no invaild input 
def ship_input():
    # Define colimn and row list that has the acceptable range for each depending on the dimension
    column=[]
    rows=[]
    for d in range(DIMENSION):
        column.append(letters[d])
        rows.append(d)
    columnrow = input("Please input the ship location eg. A3,B2,etc.: ")
    while not columnrow: # Checks if the input is empty 
        columnrow=input("Please input a vaild ship location: ")
    # Split input into column and row 
    col=columnrow[0] 
    row=columnrow[1:]
    # Checks if the user wants to end the game 
    if (col=='e' and row=='nd'):
        col='e'
        row='nd'
    # Checks if the user input is whithin the accpetable ranges of column and row
    else:
        while (row not in str(rows)) or (col not in column):
            columnrow=input("Please input a vaild ship location: ")
            row=columnrow[1:]
            col=columnrow[0]   
    return row,col

# This function initiates the game and calls all the above functions as well as operates the whole game 
def start_game():
    create_ship(Cheat_board) # Calls the function create_ship to place the ships randomly on the cheat board 
    #create_print_board(Cheat_board) This creates and prints the cheat board for reference
    ships=0
    guess=0
    end=0
    create_print_board(Game_board) # Prints the Game_board for the user 
    # Define colimn and row list that has the acceptable range for each depending on the dimension
    column=[] 
    rows=[]
    for d in range(DIMENSION):
        column.append(letters[d])
        rows.append(d)
    print( 'Welcome to Battleship')
    print('To win you are required to hit all '+ str(SHIP_SIZE)+' ships')
    print('Columns are upper case letters in the list: ',column)
    print('Rows are integer numbers in the list: ',rows)
    print('Please input your boat location in the format column letter followed by row number')
    row,col= ship_input() # Calls the function that asks the user to input ship locations
    
    '''
    This loop will act depending on the users input and it will keep looping until all ships are hit. There are 3 scenarios:
    1. The user misses where a # will be placed on the game board
    2. The user hits a ship where a X will be placed on the game board
    3. The user enters the same guess no action will be taken
    The user can end the game by typing 'end'
    The window is cleared after each trial
    '''
    while(ships < SHIP_SIZE):
        if(guess!=0):
            os.system("clear") 
            create_print_board(Game_board)
            if (trial=='same'):
                print('You already guessed this location')
            elif trial=='hit':
                print('You hit the ship')
            elif trial=='missed':
                print('You missed')
            print('Number of guesses attempted: ', guess)
            print('To terminate the game enter the word end')
            row,col= ship_input()
        if (col=='e' and row=='nd'):
            os.system("clear")
            end=1
            break
        row=int(row)
        col=letters.index(col)    
        if Game_board[row][col] == '#':
            trial='same'
        elif Cheat_board[row][col] == 'X':
            trial='hit'
            Game_board[row][col]='X'
            ships=ships+1
            guess=guess+1
        else:
            trial='missed'
            Game_board[row][col]='#'
            guess=guess+1
        if ships==SHIP_SIZE:
            os.system("clear")
            create_print_board(Game_board)
            break
        print('You have '+ str(SHIP_SIZE-ships) +' ships remaining to hit')
    return guess,end

# Called the function to start the game
# The function will return the score and if the user ended the game or not
score,end=start_game()
# The score is the number of guesses the user makes until all ships are sunk
# If the user didn't end the game then print score 
if (end==0):
    print('Congrats, you sunk all the ships')
    print('You hit all the ships in ', score,' guesses')
    print('Your score is ',score)
elif (end==1):
    print('You ended the game')
