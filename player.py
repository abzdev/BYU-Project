class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def __repr__(self):
        return "<" + self.__class__.__name__ + " name=" + str(self.name) + " letter=" + self.letter + ">"

    @staticmethod
    def input_1st_player_letter(name):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print(f'Does {name} want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def get_player_move(self, board):
        # Let the player type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.is_space_free(int(move)):
            print(f'What is {self.name}\'s next move? (1-9)')
            move = input()
        return int(move)

    def is_winner(self, bo):
        # Given a bo and a player's letter, this function returns True if that player has won.
        return ((bo.board[7] == self.letter and bo.board[8] == self.letter and bo.board[9] == self.letter) or  # across top
                (bo.board[4] == self.letter and bo.board[5] == self.letter and bo.board[6] == self.letter) or  # across middle
                (bo.board[1] == self.letter and bo.board[2] == self.letter and bo.board[3] == self.letter) or  # across bottom
                (bo.board[7] == self.letter and bo.board[4] == self.letter and bo.board[1] == self.letter) or  # down left side
                (bo.board[8] == self.letter and bo.board[5] == self.letter and bo.board[2] == self.letter) or  # down middle
                (bo.board[9] == self.letter and bo.board[6] == self.letter and bo.board[3] == self.letter) or  # down right side
                (bo.board[7] == self.letter and bo.board[5] == self.letter and bo.board[3] == self.letter) or  # diagonal
                (bo.board[9] == self.letter and bo.board[5] == self.letter and bo.board[1] == self.letter))  # diagonal
