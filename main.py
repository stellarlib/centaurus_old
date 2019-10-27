from src.game import Game, App
import sys


if __name__ == '__main__':

    app = App()
    app.initialize()

    game = Game(app)
    app.current_scene = game
    app.main()

    sys.exit()
