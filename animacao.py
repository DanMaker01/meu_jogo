
#implementar

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Formato das entradas de animação (animacao.txt):
#--------------------------------------------------------------------------------------
# índice cena
# nome_arquivo, qtd_sprites, retangulo_recorte, [indices, posicoes, escalas, rotacoes, alfas]
# .
# .
# .
# nome_ultimo, qtd_sprites, retangulo_recorte, [indices, posicoes, escalas, rotacoes, alfas]
#--------------------------------------------------------------------------------------
# Exemplo:
#--------------------------------------------------------------------------------------
# 1
# bg1, 1, [x,y,L,A], [[],[pos_1],[],[],[]]
# player1, 4, [0,0,L,A], [[0,1,2,3], [pos_1, pos_2, pos_3, pos_4], [esc_1, esc_2, esc_3, esc_4], [],[]]
#
# 2
# bg1, 1, [0,0,L,A], [[],[pos_1],[],[],[]]
# player2, 2, [0,0,L,A], [[0,1], [pos_1, pos_2, pos_3, pos_4], [esc_1, esc_2, esc_3, esc_4], [],[]]
# 
#--------------------------------------------------------------------------------------
# obs: a ordem da lista de imagem diz quem aparece atrás e quem aparece na frente.
#--------------------------------------------------------------------------------------

#sprite
class Sprite: #definir melhor o que é um sprite #implementar
    def __init__(self, imagens_id, x, y, largura, altura):
        # self.imagens = [] #imagem em sí ou img_id? #implementar
        self.imagem_id = imagens_id
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        # self.alfa = 255
        # self.transformacoes = [] #transformações aplicadas
        # self.rot_x = 0
        # self.rot_y = 0
        pass

    def draw(self, jogo):
        if self.imagem_id:
            jogo.renderer.desenhar_imagem(self.imagem_id, self.x, self.y)

    def update(self):
        pass


#
class Animacao:
    def __init__(self, _animacao_ligada = True):
        self.sprites = []
        self.frame_atual = 0
        self.t = 0
        self.animacao_ligada = _animacao_ligada

        pass

    def sprites_add(self, sprite):
        self.sprites.append(sprite)
        pass

    def animar_ligar(self):
        self.animacao_ligada = True
        pass
    def animar_desligar(self):
        self.animacao_ligada = False
        pass

    def update(self):
        if self.animacao_ligada:
            # self.sprites[self.frame_atual].update()
            if self.t % 10 == 0:
                self.avancar_sprite()
            self.t+=1
        pass

    def avancar_sprite(self):
        self.frame_atual += 1
        if self.frame_atual >= len(self.sprites):
            self.frame_atual = 0
            pass
        pass
    
    def get_sprite_atual(self)->Sprite: 
        return self.sprites[self.frame_atual]
    

