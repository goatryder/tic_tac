from Board import Board
from BoardView import BoardView
from Game import Game
from Player import Player


def main():
    # models
    player1 = Player(str(input("Enter player1 name:\t")))
    player2 = Player(str(input("Enter player2 name:\t")))
    board = Board()

    # initialize controller
    game = Game(board, player1, player2, BoardView)

    while True:
        game.play()


if __name__ == "__main__":
    main()
