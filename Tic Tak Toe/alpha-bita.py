def printBoard(board):
    """Prints the current state of the 4x4 board."""
    for i in range(1, 17, 4):
        print(board[i] + '|' + board[i+1] + '|' + board[i+2] + '|' + board[i+3])
        if i < 13:
            print('-+-+-+-')
    print("\n")


def spaceIsFree(position):
    """Checks if a given position on the board is free."""
    return board[position] == ' '


def insertLetter(letter, position):
    """Inserts the letter (either 'X' or 'O') at the given position on the board."""
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        
        if checkDraw():
            print("Draw!")
            exit()
        
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)


def checkForWin():
    """Checks if there is a win condition on the board (4 in a row)."""
    # Possible winning positions for 4x4 grid
    winning_positions = [
        # Rows
        (1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16),
        # Columns
        (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (4, 8, 12, 16),
        # Diagonals
        (1, 6, 11, 16), (4, 7, 10, 13)
    ]
    
    # Check all winning positions for a win
    return any(board[a] == board[b] == board[c] == board[d] != ' ' for a, b, c, d in winning_positions)


def checkDraw():
    """Checks if the board is full, indicating a draw."""
    return all(board[key] != ' ' for key in board.keys())


def playerMove():
    """Handles the player's move by asking for a position and placing 'O'."""
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)


def compMove():
    """Handles the computer's move using the minimax algorithm with alpha-beta pruning."""
    bestScore = -800
    bestMove = 0
    
    # Evaluate each possible move for the computer
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot  # Place 'X' temporarily
            score = minimax(board, 0, False, -800, 800)  # Get minimax score
            board[key] = ' '  # Undo move
            
            # Update best move if the current move has a higher score
            if score > bestScore:
                bestScore = score
                bestMove = key
    
    insertLetter(bot, bestMove)  # Make the best move


MAX_DEPTH = 4  # Set a maximum depth for depth-limited search

def minimax(board, depth, isMaximizing, alpha, beta):
    """
    Minimax algorithm with alpha-beta pruning and depth limiting.
    
    Parameters:
        board (dict): Current game board.
        depth (int): Current depth of the recursion.
        isMaximizing (bool): True if the current player is the maximizer.
        alpha (int): Alpha value for alpha-beta pruning.
        beta (int): Beta value for alpha-beta pruning.
    
    Returns:
        int: The score of the current board position.
    """
    # Base cases
    if checkForWin():
        return 1 if isMaximizing else -1  # Score based on who wins
    elif checkDraw():
        return 0  # Draw returns 0 score
    elif depth >= MAX_DEPTH:
        return 0  # Depth limit reached; return neutral score

    if isMaximizing:
        # Maximizing player (Bot)
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False, alpha, beta)
                board[key] = ' '
                bestScore = max(score, bestScore)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cutoff
        return bestScore
    else:
        # Minimizing player (Player)
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True, alpha, beta)
                board[key] = ' '
                bestScore = min(score, bestScore)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha cutoff
        return bestScore


# Initialize the 4x4 board
board = {i: ' ' for i in range(1, 17)}

# Display initial board and instructions
printBoard(board)
print("Player goes first! Good luck.")
print("Positions are as follows:")
print("1, 2, 3, 4 ")
print("5, 6, 7, 8 ")
print("9, 10, 11, 12 ")
print("13, 14, 15, 16 ")
print("\n")

# Define player and bot markers
player = 'O'
bot = 'X'

# Game loop: Player and computer take turns
while not checkForWin():
    playerMove()  # Player's turn
    if not checkForWin():
        compMove()  # Computer's turn
