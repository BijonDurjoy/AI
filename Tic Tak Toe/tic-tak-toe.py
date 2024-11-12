# Function to print the current state of the game
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

# Function to check if a given board position is free
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

# Function to insert a letter ('X' or 'O') at a given position on the board
# Checks if the position is free before inserting
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board) # Print the board

         # Check for a draw after the move
        if (checkDraw()):
            print("Draw!")
            exit()

        # Check if this move won the game    
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return

    # If the chosen position is not free, prompt the player to enter a new one
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

# Function to check if the current board state has a winning condition
def checkForWin():
    #Check all posible winning combination
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# Function to check if the board is full, indicating a draw
def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

# Function to check if the board is full, indicating a draw
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

# Function for the computer's move, uses the minimax algorithm to determine the best move
def compMove():
    bestScore = -800
    bestMove = 0

    # Evaluate all possible moves on the board
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

# Minimax algorithm to evaluate the best possible moves for the bot
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        # Try all empty spots for maximizing (bot) player
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        # Try all empty spots for minimizing (player) player
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

# Initialize the Tic-Tac-Toe board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Display initial game instructions
printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

# Set symble for bot and player
player = 'O'
bot = 'X'

global firstComputerMove
firstComputerMove = True

while not checkForWin():
    playerMove()
    compMove()