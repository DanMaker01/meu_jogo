# ----------------------------------------------------------------------------
# 01/09/2024
# DanMaker
# ----------------------------------------------------------------------------

# imports
import os
from jogo import Jogo

# ----------------------------------------------------------------------------
# consegue o tamanho total da tela
x = 0
y = 32
canto_ou_centro = 'canto'

if canto_ou_centro == 'centro':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
else:
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(x) + "," + str(y)


# Define a posição da janela (x, y)


if __name__ == "__main__":
    game = Jogo()
    game.run()
