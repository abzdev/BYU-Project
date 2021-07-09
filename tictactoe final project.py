# Tic Tac Toe

import random
import tttgame
from tttgame import basicTicTacToe

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = tttgame.inputPlayerLetter()
    turn = tttgame.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            tttgame.drawBoard(theBoard)
            move = tttgame.getPlayerMove(theBoard)
            tttgame.makeMove(theBoard, playerLetter, move)

            if tttgame.isWinner(theBoard, playerLetter):
                tttgame.drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if tttgame.isBoardFull(theBoard):
                    tttgame.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = tttgame.getComputerMove(theBoard, computerLetter)
            tttgame.makeMove(theBoard, computerLetter, move)

            if tttgame.isWinner(theBoard, computerLetter):
                tttgame.drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if tttgame.isBoardFull(theBoard):
                    tttgame.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not tttgame.playAgain():
        break
