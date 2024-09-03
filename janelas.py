# classe Janelas

import pygame

class Janela:
    def __init__(self,jogo, x, y, largura, altura, ativa=False, texto="", cor=(255, 255, 170)):
        print("iniciou classe Janela")
        self.jogo = jogo
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        
        self.cor = cor
        
        self.ativa = ativa

        self.texto = texto
        pass

    def draw(self):
        #desenha um retangulo na janela
        pygame.draw.rect(self.jogo.screen, self.cor, (self.x, self.y, self.largura, self.altura))

        if self.texto != "":
            #desenha um texto na janela
            label = self.jogo.font.render(self.texto, 1, (0, 0, 0))
            margemx = self.largura/2 - label.get_width()/2
            margemy = self.altura/2 - label.get_height()/2
            self.jogo.screen.blit(label, (self.x+margemx, self.y+margemy))
        
        pass