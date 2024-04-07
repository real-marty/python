import numpy as np
import utils
from utils import Player, evaluate_board_state


class MinimaxPlayer(Player):
    def __init__(self):
        super().__init__()
        self.tic_tac_toe_depth = 9
        self.gemoku_depth = 2
        self.score_dic = {
            (1, 1): 1,
            (1, 2): 5,
            (2, 1): 5,
            (2, 2): 100,
            (3, 1, "S"): 150,
            (3, 2, "S"): 1000,
            (3, 1): 1000,
            (3, 2): 10000,
            (4, 0, "S"): 10000,
            (4, 1, "S"): 15000,
            (4, 2, "S"): 100000,
            (4, 1): 200000,
            (4, 2): 1000000}
        
        
    def first_move_center(self, board):
        center_row = board.shape[0] // 2
        center_col = board.shape[1] // 2    
        return (center_row, center_col)

    def next_move(self, board: np.ndarray):
        if np.all(board == 0):
            return self.first_move_center(board)
        return self.best_move(board, self.MARKER)

    
    def best_move(self, board: np.ndarray, player: int):
        if utils.WIN_STATE_LEN == 3:
            best_score, move = self.minimax_with_pruning(board, self.tic_tac_toe_depth, player, -np.inf, np.inf, self.heuristic_evaluation_3x3)
        else:
            best_score, move = self.minimax_with_pruning(board, self.gemoku_depth, player, -np.inf, np.inf, self.heuristic_evaluation_9x9)
        print(f"best AI score: {best_score}")
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
        """
        Simple heuristic for Tic-Tac-Toe.
        
        :param board: 2D numpy array representing the game board. 1 for player 1's marks, -1 for player 2's marks, and 0 for empty.
        :param player: The player for whom to evaluate the board. 1 or -1.
        :return: heuristic value indicating how favorable the board is to the specified player.
        """
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


    def heuristic_evaluation_9x9(self, board, player):
        score = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Horizontal, Vertical, Diagonal, Anti-Diagonal
        for row in range(9):
            for col in range(9):
                if board[row, col] == player:
                    for direction in directions:
                        temp_score, open_ends = self.evaluate_direction(board, row, col, player, direction)
                        # Update to use score_dict
                        score_key = (temp_score, open_ends)
                        if score_key in self.score_dic:
                            score += self.score_dic[score_key]
                        elif (temp_score, open_ends, "S") in self.score_dic:  # Check for soft sequence
                            score += self.score_dic[(temp_score, open_ends, "S")]
        return score



    def evaluate_direction(self, board, row, col, player, direction):
        consecutive_count = 1
        open_ends = 0
        steps = [1, -1]  # Check in both directions

        for step in steps:
            r, c = row + (step * direction[0]), col + (step * direction[1])
            while 0 <= r < 9 and 0 <= c < 9 and board[r, c] == player:
                consecutive_count += 1
                r += step * direction[0]
                c += step * direction[1]

            # Check if the end is open
            if 0 <= r < 9 and 0 <= c < 9 and board[r, c] == 0:
                open_ends += 1
            elif r < 0 or r >= 9 or c < 0 or c >= 9:
                open_ends += 1  # Consider board edge as an open end

        return consecutive_count, open_ends
    
