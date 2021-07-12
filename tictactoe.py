# Tic Tac Toe

import random
from board import Board
from player import Player


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def who_goes_first():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = Board([' '] * 10)
    player1Letter, player2Letter = Player.input_1st_player_letter()
    player1 = Player('Player 1', player1Letter)
    player2 = Player('Player 2', player2Letter)
    turn = who_goes_first()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player1':
            # Player 1's turn.
            theBoard.draw_board()
            move = player1.get_player_move(theBoard)
            theBoard.make_move(player1.letter, move)

            if theBoard.is_winner(player1.letter):
                theBoard.draw_board()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if theBoard.is_board_full():
                    theBoard.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            # Player 2's turn.
            theBoard.draw_board()
            move = player2.get_player_move(theBoard)
            theBoard.make_move(player2.letter, move)

            if theBoard.is_winner(player2.letter):
                theBoard.draw_board()
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if theBoard.is_board_full():
                    theBoard.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not play_again():
        break
