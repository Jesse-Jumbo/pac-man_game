from module.settings import *
from module.Game import Game



# create the game object

game = Game()
game.show_start_screen()

while True:
    game.new()
    game.run()
