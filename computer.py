class Computer:
    def __init__(self):
        pass

    def get_computer_move(self, ttt_board, computer_letter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computer_letter == 'X':
            player_letter = 'O'
        else:
            player_letter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = ttt_board.get_board_copy()
            if copy.is_space_free(i):
                copy.make_move(computer_letter, i)
                if copy.is_winner(computer_letter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = ttt_board.get_board_copy()
            if copy.is_space_free(i):
                copy.make_move(player_letter, i)
                if copy.is_winner(player_letter):
                    return i

        # Try to take one of the corners, if they are free.
        move = ttt_board.choose_random_move_from_list([1, 3, 7, 9])
        if move is not None:
            return move

        # Try to take the center, if it is free.
        if ttt_board.is_space_free(5):
            return 5

        # Move on one of the sides.
        return ttt_board.choose_random_move_from_list([2, 4, 6, 8])
