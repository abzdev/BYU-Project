# Tic Tac Toe

import random
from board import Board
from player import Player
from computer import Computer


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def who_goes_first():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = Board([' '] * 10)
    computer = Computer()
    playerLetter, computerLetter = Player.input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':
            # Player's turn.
            theBoard.draw_board()
            move = Player.get_player_move(theBoard)
            theBoard.make_move(playerLetter, move)

            if theBoard.is_winner(playerLetter):
                theBoard.draw_board()
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if theBoard.is_board_full():
                    theBoard.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = computer.get_computer_move(theBoard, computerLetter)
            theBoard.make_move(computerLetter, move)

            if theBoard.is_winner(computerLetter):
                theBoard.draw_board()
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if theBoard.is_board_full():
                    theBoard.draw_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
