# imports
import os
from jogo import Jogo

# ----------------------------------------------------------------------------
# Define a posição da janela (x, y)
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,32"


if __name__ == "__main__":
    game = Jogo()
    game.run()
