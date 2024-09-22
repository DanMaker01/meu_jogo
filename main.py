# ----------------------------------------------------------------------------
# 01/09/2024
# DanMaker
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# TO-DO
# 
# ------------------PRIORIDADE
#
# - barra de tempo, primeiro em vaores depois em sprites
#  
# - definir classe Sprite melhor
#
# 
# 
#
#
#
#
# - desenhar no papel como vai ser uma história de 30 cenas
# - definir estrutura de historia principal, como será 1 dia.
#
#
#
#
#
#
#
#
#
#
#   
# -------------------LEGAL MAS NÃO ESSENCIAL
#
# - fazer alterações profundas no roteiro, como definir melhor os efeitos de animação, velocidade da Pressão
# - modificar o roteiro para definir mais coisas, como a velocidade
#
#
#
# - criar classe animação
#       lista_sprites = []
#       frame_atual = 0
#       animado = True
#
# - criar classe sprite
#       img
#       translação, escala, rotação 
#       origem
#       cor
#       alpha
#
# - criar classe gerenciadorAnimação
#       camadas = [] 
#       camada_add_sprite(camada, sprite)
#       camada_rem_sprite(camada, sprite)
#       camadas_desenhar_todas()
#       camada_desenhar()
#       update
#       
#       
# - mostrar parcialmente uma opção se você tiver parte dos requisitos
# 
# - adicionar lista de condições
# - adicionar lista de itens quando escolher uma opção
#
#
# - montar time de
#       eu
#       você
#       zoboomafoo
#
# - ao sair do jogo, abrir janela perguntando se vc quer salvar
#
# 
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
# - pequenas variações nas cenas de forma procedural.            
#
#
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
# - fazer história principal, usando a repetição dos dias onde pequenas variações acontecem no cotidiano das cenas que dá uma ideia maior.
#
# - polir o jogo para lançar (mesmo que com coisa faltando)
# ----------------------------------------------------------------------------
# ==================================================================================


# imports
import os
from jogo import Jogo

# Define a posição (x, y) da janela no windows
canto_ou_centro = 'canto' # inicia janela centralizado ou no canto superior-esquerdo
x = 64
y = 32

if canto_ou_centro == 'centro':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
else:
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(x) + "," + str(y)


if __name__ == "__main__":
    game = Jogo()
    game.run()
