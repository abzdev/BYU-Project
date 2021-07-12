class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    @staticmethod
    def input_1st_player_letter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Does Player 1 want to be X or O?')
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
