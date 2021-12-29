from module.setting import *
from module.Game import Game



# create the game object

game = Game()
game.show_start_screen()

while True:
    game.new()
    game.run()
    game.show_go_screen()
