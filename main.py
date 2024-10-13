# ----------------------------------------------------------------------------
# 01/09/2024
# DanMaker
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# a fazer:
# ----------------------------------------------------------------------------
# ------------------PRIORIDADE
#
#
# - desenhar no papel como vai ser uma história de 20 cenas
#       - se forem 4x de 20 cenas = 80 cenas num dia
#       - se forem 5 dias são 5x 80 = 400 cenas 
#
#
#
# - definir estrutura de historia principal, como será 1 dia.
#       - 1a atividade: ir para o trabalho
#       - 2a atividade: fazer o trabalho
#       - 3a atividade: voltar para casa
#       - 4a atividade: dormir(?)
# 
#
# - fazer um hub da cidade onde dá pra escolher o lugar que vc vai
#       ir pro trabalho
#       ir para casa
#       + 1 lugar(?)
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
#
#
# - definir classe Sprite melhor, diferenciar de Animação
#       imagem[]
#       translação, escala, rotação 
#       origem
#       cor
#       alpha
#
# - criar classe animação, diferenciar de sprite
#       importar_sprites
#       importar_transformacoes
#       animado = True
#       
#       lista_sprites = []              (os elementos são sprite_i )
#       lista_transformacoes = []       (os elementos são [s,r,t] )
#       
#       frame_atual = 0
#       frame_avancar()
#       desenhar()
#
# - criar classe gerenciadorAnimação (saber trabalhar com BG)
#       ativado = True
#       lista_camadas = [] (em cada camada, suas animações)
#       
#       tempo_atual
#       tempo_avancar() 
#       
#       camada_add_anima(camada, anima)
#       camada_rem_anima(camada, anima)
#       camada_desenhar()
#       camadas_desenhar_todas()
#       update
#       
# - fazer alterações profundas no roteiro, como definir melhor os efeitos de animação
#
# - modificar o roteiro.txt para definir mais coisas, como:
#       velocidade (???), 
#       animação, 
#       sprites, 
#       talvez valha criar anima.txt para controlar as posições dos sprites, acho que vale hein:
#           pontos positivos:
#               - estrutura bem definida, cada cena terá um id em anima.txt, em cada um destes vai ter N animações com  
#
#
#
# - tentar criar uma classe que cuide de eventos de tempo sequenciais, como em GerenciadorCena
#
# - editor de roteiro separado, integrando img_cena, texto, opções, variáveis, que salve e load roteiros
#
# - mostrar parcialmente uma opção se você tiver parte dos requisitos
#
#       
#       
# 
# - adicionar lista de condições(?)                             << acho que já está finalizado
# - adicionar lista de itens quando escolher uma opção(?)       << acho que já está finalizado
#
#
# - montar time de
#       SOLO!           EQUIPE!
#       eu              eu
#                       você
#                       zoboomafoo
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
# - interface para Mouse
#
#
# - corrigir os bugs do alpha para o Palco
#
# -------------------- FINALIZA QUANDO
#
# - completar uma história de 20 cenas
#
# - completar duas histórias de 20 cenas
#
# - completar três histórias de 20 cenas
#
# - completar quatro histórias com 20 cenas - isso equivale a um dia
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
