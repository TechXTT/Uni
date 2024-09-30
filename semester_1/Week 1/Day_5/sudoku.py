import numpy as np

# Function to read the Sudoku board from a file
def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            # Replace '.' with 0 and strip any extra spaces
            row = []
            for char in line:
                if char == '.':
                    row.append(0)
                elif char.isdigit():
                    row.append(int(char))
            print(row)
            if row:
                board.append(row)
    return board

# Function to check if it's valid to place a number in a given position
def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Function to find the next empty cell (returns row, col)
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Recursive function to solve the board
def solve(board):
    empty = find_empty(board)
    if not empty:
        # No more empty spots, puzzle solved
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            # Recursively try to fill the rest of the board
            if solve(board):
                return True
            # If placing num doesn't lead to a solution, reset it
            board[row][col] = 0

    return False

# Main function to solve the Sudoku from the file
def main():
    board = read_board_from_file('./s.txt')
    print("Initial Board:")
    print(np.matrix(board))
    
    if solve(board):
        print("Solved Board:")
        print(np.matrix(board))
    else:
        print("No solution exists")

# Run the main function
if __name__ == "__main__":
    main()