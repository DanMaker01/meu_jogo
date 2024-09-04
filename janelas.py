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
        pass

    def ativar(self):
        self.ativa = True
        pass
    def desativar(self):
        self.ativa = False
        pass

    def draw(self, jogo):
        #desenha um retangulo na janela
        pygame.draw.rect(jogo.screen, self.cor, (self.x, self.y, self.largura, self.altura))

        if self.texto != "":
            #desenha um texto na janela
            label = jogo.font.render(self.texto, 1, (0, 0, 0))
            margemx = self.largura/2 - label.get_width()/2
            margemy = self.altura/2 - label.get_height()/2
            jogo.screen.blit(label, (self.x+margemx, self.y+margemy))
        
        pass

    def set_cor(self, cor):
        self.cor = cor
        pass
    def set_cor_original(self):
        self.cor = self.cor_coriginal
        pass