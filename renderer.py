# implementar Animação (ao invés de renderer.py)

import pygame

class Renderer:
    def __init__(self,jogo):
        self.jogo = jogo
        self.controle = jogo.controle

        self.cor_neutra = (0, 0, 0)
        
        self.font = jogo.font
        self.font_color = (20,20,20)
        self.margem_x = 10
        self.margem_y = 10
        self.espacamento_linhas = 20
        pass
    
    def desenhar_bg(self):
        imagem = self.jogo.recursos.get_img(0) # a imagem 0 é o BG
        self.jogo.screen.blit(imagem, (0,0))
        pass

    
    def desenhar_imagem(self, indice_imagem, x, y):
        imagem = self.jogo.recursos.get_img(indice_imagem)
        self.jogo.screen.blit(imagem, (x, y), (0,0,imagem.get_width(),imagem.get_height()))
        pass    

    def desenhar_texto(self, texto, x, y):
        label = self.font.render(texto, 1, self.font_color)
        self.jogo.screen.blit(label, (x, y))
        pass


    def desenhar_hud(self):
        # 
        texto_1 = "FPS: "+str(self.jogo.clock.get_fps())
        label = self.font.render(texto_1, 1, self.font_color)
        self.jogo.screen.blit(label, (self.margem_x, self.margem_y))
        # Texto dinâmico
        texto_2 = "cena: "+str(self.jogo.gerenciador_cena.get_cena_atual_id())
        label = self.font.render(texto_2, 1, self.font_color)
        self.jogo.screen.blit(label, (self.margem_x, self.margem_y + self.espacamento_linhas))
        # lista de janelas para renderizar
        
        pass
