import numpy as np
import utils
from utils import Player, evaluate_board_state


class MinimaxPlayer(Player):
    def __init__(self):
        super().__init__()
        self.tic_tac_toe_depth = 9
        
        
    def first(self, board):
        center_row = board.shape[0] // 2
        center_col = board.shape[1] // 2    
        return (center_row, center_col)

    def next_move(self, board: np.ndarray):
        if np.all(board == 0):
            return self.first(board)
        return self.best_move(board, self.MARKER)

    
    def best_move(self, board: np.ndarray, player: int):
        _, move = self.minimax_with_pruning(board, self.tic_tac_toe_depth, player, -np.inf, np.inf, self.heuristic_evaluation_3x3)
        return move
    
    def minimax_with_pruning(self, board, depth, player, alpha, beta, heuristic_evaluation):
        game_end, winner = evaluate_board_state(board)  
        
        if game_end:
            return self.score(winner), None
        if depth == 0:
            return heuristic_evaluation(board, player), None
        
        is_maximizing = player == self.MARKER
        best_score = -np.inf if is_maximizing else np.inf
        best_move = None

        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if board[row][col] == 0:  # Check if the cell is empty
                    board[row][col] = player  # Make a move
                    score, _ = self.minimax_with_pruning(board, depth-1, -player, alpha, beta, heuristic_evaluation)
                    board[row][col] = 0  # Undo the move
                    if is_maximizing:
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
                        alpha = max(alpha, best_score)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (row, col)
                        beta = min(beta, best_score)
            if beta <= alpha:
                break

        return best_score, best_move    

    def score(self, winner):
        if winner is None:
            return 0  # Draw
        elif winner == self.MARKER:
            return 1  # AI wins
        else:
            return -1  # Opponent wins
        
    def heuristic_evaluation_3x3(self, board, player):  
        if player != -1 and player != 1:
            raise ValueError("Player must be 1 or -1")

        def check_line(line):
            """Check a line (row, column, or diagonal) for scoring potential."""
            if player in line and -player not in line:
                return 10  # Good line for player
            elif -player in line and player not in line:
                return -10  # Good line for opponent
            return 0  # Neutral or blocked line

        score = 0
        # Check rows and columns
        for i in range(3):
            score += check_line(board[i, :])  # Check row
            score += check_line(board[:, i])  # Check column

        # Check diagonals
        score += check_line(np.diag(board))
        score += check_line(np.diag(np.fliplr(board)))

        return score