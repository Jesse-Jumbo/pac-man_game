from module.settings import *
from module.Game import Game



# create the game object

game = Game()
game.__init__()
while True:
    game.run()

