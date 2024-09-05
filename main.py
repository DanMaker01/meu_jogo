# ----------------------------------------------------------------------------
# 01/09/2024
# DanMaker
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# TO-DO
# - mudar layout da cena, 
#       imagem principal alinhada a esquerda (320x360)
#       texto alinhado à direita 120x160 (160 ou mais)
#       opções alinhadas a direita 120x160 (160 ou menos)
#
# - fazer aparecer em ordem, janela_princpal, texto, opcoes e liberar interação @@@@@@@@
#
# - dividir melhor as classes e funções
#
# - adicionar modificadores ao escolher certas ações
#       modificadores são adicionados numa lista quando você faz uma escolha especial
#       os modificadores são tratados como itens, 
#       caso você receba um modificador ele é adicionado na lista, com multiplicidade
#       caso você receba novamente algum modificador só é acrescido seu numero no inventário
#  
# - completar uma história de 30 cenas
#
# - completar duas histórias de 30 cenas
#
# - completar três histórias de 30 cenas
#
# - completar um dia (ciclo de 4 atividades)
# 
# - fazer história usando a repetição de cenas dos dias, sentimento de repetição, monotonia 
#
# - polir o jogo
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# imports
import os
from jogo import Jogo

# Define a posição da janela (x, y)
x = 0
y = 32
canto_ou_centro = 'canto'

if canto_ou_centro == 'centro':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
else:
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(x) + "," + str(y)


if __name__ == "__main__":
    game = Jogo()
    game.run()
