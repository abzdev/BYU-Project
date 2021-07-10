# Tic Tac Toe

import random
import tttgame
#from tttgame import basicTicTacToe

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = tttgame.inputPlayerLetter()
    turn = tttgame.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player's turn.
            tttgame.drawBoard(theBoard)
            move = tttgame.getPlayerOneMove(theBoard)
            tttgame.makeMove(theBoard, playerLetter, move)

            if tttgame.isWinner(theBoard, playerLetter):
                tttgame.drawBoard(theBoard)
                print('player1 has beaten player2!')
                gameIsPlaying = False
            else:
                if tttgame.isBoardFull(theBoard):
                    tttgame.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            tttgame.drawBoard(theBoard)
            move = tttgame.getPlayerTwoMove(theBoard)
            tttgame.makeMove(theBoard, computerLetter, move)

            if tttgame.isWinner(theBoard, computerLetter):
                tttgame.drawBoard(theBoard)
                print('player2 has beaten player1!')
                gameIsPlaying = False
            else:
                if tttgame.isBoardFull(theBoard):
                    tttgame.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not tttgame.playAgain():
        break
