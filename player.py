class Player:
    def __init__(self):
        pass

    @staticmethod
    def input_player_letter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    @staticmethod
    def get_player_move(board):
        # Let the player type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.is_space_free(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)
