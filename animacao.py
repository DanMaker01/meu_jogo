

#sprite
class Sprite: #definir melhor o que é um sprite #implementar
    def __init__(self, imagens_id, x, y, largura, altura):
        # self.imagens = [] #imagem em sí ou img_id? #implementar
        self.imagem_id = imagens_id
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rot_x = 0
        self.rot_y = 0
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