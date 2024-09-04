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
# - adicionar sistema de guardar histórico, arvore de cenas, save e load
#
# - fazer aparecer em ordem, janela_princpal, texto, opcoes e liberar interação
#
# - dividir melhor as classes e funções
#
# - adicionar modificadores ao escolher certas ações
#       modificadores são adicionados numa lista quando você faz uma escolha especial
#       os modificadores são tratados como itens, 
#       caso você receba um modificador ele é adicionado na lista, com multiplicidade
#       caso você receba novamente algum modificador só é acrescido seu numero no inventário
#  
# - completar uma história de 20 cenas
#
# - completar um dia (ciclo de 8 atividades)
# 
# - fazer história usando a repetição de cenas dos dias, sentimento de repetição, monotonia 
# - poli
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# imports
import os
from jogo import Jogo

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
