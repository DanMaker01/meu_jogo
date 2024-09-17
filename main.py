# ----------------------------------------------------------------------------
# 01/09/2024
# DanMaker
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# TO-DO
# 
# ------------------PRIORIDADE
#
# - adicionar modificadores ao escolher certas ações
#       modificadores são adicionados numa lista quando você faz uma escolha especial
#       os modificadores são tratados como itens, 
#       caso você receba um modificador ele é adicionado na lista, com multiplicidade
#       caso você receba novamente algum modificador só é acrescido seu numero no inventário
#
# 
# #
# #
# #
# #  
# -------------------LEGAL MAS NÃO ESSENCIAL
# - mudar layout da cena, 
#       imagem principal alinhada a esquerda (320x360)
#       texto alinhado à direita 120x160 (160 ou mais)
#       opções alinhadas a direita 120x160 (160 ou menos)
#       deixar com 3 opções de layout
#
# - corrigir os bugs do alpha para o Palco
#
# - implementar uma lista de janelas controladas pelo gerenciador de janelas, além de palco,texto,opcoes
#       pra q?
# 
# - definir melhor as classes, organizar funcionamento interno em uma lista com prioridades rodada numa função principal.
#       - definir o que é uma Janela, se ela pode comportar texto e imagem
#           estou tendendo a deixar a janela apenas com o básico de uma janela:
#           cor-RGBA, pos(X,Y), dimensao(L,A), ativação(tempo, bool, funções), 
#       listar quais classes precisa:
#           retangulo
#           gerenciador de janelas geral
#           janela
#              
#

# -------------------- FINALIZA QUANDO
#
# - completar uma história de 30 cenas
#
# - completar duas histórias de 30 cenas
#
# - completar três histórias de 30 cenas
#
# - completar quatro histórias com 30 cenas - isso equivale a um dia
# 
# - fazer história principal usando a repetição dos dias, sentimento de repetição, monotonia 
#
# - polir o jogo para lançar (mesmo que com coisa faltando)
# ----------------------------------------------------------------------------
# ==================================================================================


# imports
import os
from jogo import Jogo

# Define a posição (x, y) da janela no windows
canto_ou_centro = 'canto' # inicia janela centralizado ou no canto superior-esquerdo
x = 0
y = 32

if canto_ou_centro == 'centro':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
else:
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(x) + "," + str(y)


if __name__ == "__main__":
    game = Jogo()
    game.run()
