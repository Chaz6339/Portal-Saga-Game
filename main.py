from game import Game
from gameboard import GameBoard

game = Game()
gui = GameBoard("The Portal Saga", game, Game.SIZE)
gui.run()
