import random


class Board:
    def __init__(self, board):
        self.board = board

    def draw_board(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def get_board_copy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupe_board = Board([])

        for i in self.board:
            dupe_board.board.append(i)

        return dupe_board

    def is_space_free(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def is_board_full(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.is_space_free(i):
                return False
        return True

    def make_move(self, letter, move):
        self.board[move] = letter

    def is_winner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or  # across the top
                (self.board[4] == le and self.board[5] == le and self.board[6] == le) or  # across the middle
                (self.board[1] == le and self.board[2] == le and self.board[3] == le) or  # across the bottom
                (self.board[7] == le and self.board[4] == le and self.board[1] == le) or  # down the left side
                (self.board[8] == le and self.board[5] == le and self.board[2] == le) or  # down the middle
                (self.board[9] == le and self.board[6] == le and self.board[3] == le) or  # down the right side
                (self.board[7] == le and self.board[5] == le and self.board[3] == le) or  # diagonal
                (self.board[9] == le and self.board[5] == le and self.board[1] == le))  # diagonal

    def choose_random_move_from_list(self, moves_list):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possible_moves = []
        for i in moves_list:
            if self.is_space_free(i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None
