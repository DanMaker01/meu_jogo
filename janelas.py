# classe Janelas

import pygame

class Janela:
    def __init__(self, x, y, largura, altura, ativa=False, texto="", cor=(255, 255, 170)):
        # print("iniciou classe Janela")
        # self.jogo = jogo
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        
        self.cor = cor
        self.cor_coriginal = cor
        self.ativa = ativa

        self.texto = texto

        self.luz = 0.0 ###  [0,1]
        self.flag_ativa_luz = 0
        self.luz_incremento = 0
        pass

    def iluminar(self, tempo_milisegundos= 200):
        self.flag_ativa_luz = tempo_milisegundos
        self.luz_incremento = 1/tempo_milisegundos
        pass
    
    def ativar(self):
        self.ativa = True
        pass
    def desativar(self):
        self.ativa = False
        
        pass

    def draw(self, jogo):
        #desenha um retangulo na janela
        cor = (self.luz* self.cor[0],  self.luz*  self.cor[1],  self.luz*  self.cor[2])

        if self.ativa:
            pygame.draw.rect(jogo.screen, cor, (self.x, self.y, self.largura, self.altura))

        

        if self.texto != "":
            #desenha um texto na janela
            label = jogo.font.render(self.texto, 1, (0, 0, 0))
            margemx = self.largura/2 - label.get_width()/2
            margemy = self.altura/2 - label.get_height()/2
            jogo.screen.blit(label, (self.x+margemx, self.y+margemy))
    
        pass

    def update(self):
        if self.flag_ativa_luz > 0:
            self.flag_ativa_luz -= 1
            self.luz = min(1, self.luz + self.luz_incremento)
            # print(self.luz, self.cor)
        pass

    def set_cor(self, cor):
        self.cor = cor
        pass
    def get_cor(self):
        return self.cor
    def set_cor_original(self):
        self.cor = self.cor_coriginal
        pass
    def set_texto(self, texto):
        self.texto = texto
        pass
    def get_texto(self):
        return self.texto