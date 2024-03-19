


def solve_queens(board):
    """
    Solves the N-queens problem using backtracking. 
    """
    solutions = []

    def backtrack(row):
        """Backtracks to find all valid placements of queens."""

        if row == 4:  
            solutions.append([queen.copy() for queen in board]) 
            return

        for col in range(4):
            if is_valid(board, row, col):
                board[row][col] = row + 1  # Place the queen
                backtrack(row + 1)  # Recursively place remaining queens
                board[row][col] = 0  # Backtrack

    def is_valid(board, row, col):
        """Checks if a queen can be placed at the given position."""

        # Check rows and columns
        for i in range(4):
            if board[i][col] != 0 or board[row][i] != 0:
                return False

        # Check diagonals
        for i in range(1, min(row, col) + 1):
            if row - i >= 0 and col - i >= 0 and board[row - i][col - i] != 0:  # Check left upper 
                return False
            if row + i < 4 and col + i < 4 and board[row + i][col + i] != 0:  # Check right lower
                return False

        return True

    backtrack(0)
    return solutions

# Example usage
board = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
solutions = solve_queens(board)
print(f"Number of solutions: {len(solutions)}")
# Print all solutions (each solution is a 4x4 list representing the board)
for solution in solutions:
  for row in solution:
    print(row)
  print()
