def printBoard(board):
    """
    Prints the chessboard configuration with queens.
    """
    for row in board:
        print(" ".join(row))
    print("\n")


def isSafe(board, row, col, n):
    """
    Checks if placing a queen at (row, col) is safe.
    """
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solveNQueens(board, row, n):
    """
    Recursively attempts to place queens on the board.
    """
    # Base case: If all queens are placed, we found a solution
    if row == n:
        printBoard(board)
        return True

    # Try placing a queen in each column in the current row
    for col in range(n):
        if isSafe(board, row, col, n):
            # Place the queen
            board[row][col] = 'Q'

            # Recursively place queens in the next row
            if solveNQueens(board, row + 1, n):
                return True

            # If placing queen in (row, col) doesn't lead to a solution,
            # backtrack and remove the queen
            board[row][col] = '.'

    # If no column is safe, return False
    return False


# Initialize an empty 8x8 board
n = 8
board = [['.' for _ in range(n)] for _ in range(n)]

# Attempt to solve the 8-Queens problem
if not solveNQueens(board, 0, n):
    print("No solution found.")
