# Tic Tac Toe

import random
from board import Board
from player import Player


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def who_goes_first(p1, p2):
    # Randomly choose the player who goes first.
    return p1.name if random.randint(0, 1) == 0 else p2.name


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = Board([' '] * 10)
    name1 = input("Enter the first player's name: ")
    name2 = input("Enter the second player's name: ")
    player1Letter, player2Letter = Player.input_1st_player_letter()
    player1 = Player(name1, player1Letter)
    player2 = Player(name2, player2Letter)
    turn = who_goes_first(player1, player2)
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
                print(f'Hooray! {player1.name} has won the game!')
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
                print(f'Hooray! {player2.name} has won the game!')
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
