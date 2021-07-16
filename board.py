class Board:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return "<" + self.__class__.__name__ + " board=" + str(self.board) + ">"

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
