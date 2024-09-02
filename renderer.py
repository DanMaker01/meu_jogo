import pygame

class Renderer:
    def __init__(self, screen, font, recursos):
        # self.bg_renderer = BackgroundRenderer(screen, recursos)
        # self.hud_renderer = HUDRenderer(screen, font, timeline, database, input)
        # self.player_renderer = PlayerRenderer(screen, recursos, timeline, larg, alt)
        self.recursos = recursos
        self.screen = screen
        self.cor_neutra = (0, 0, 0)

    def desenhar_bg(self):
        imagem = self.recursos.get_img(0)
        self.screen.blit(imagem, (0,0))

    def draw(self):
        self.screen.fill(self.cor_neutra)  # Preenche a tela com a cor cinza
        self.desenhar_bg()  # Renderizar o fundo
        # self.player_renderer.desenhar_jogador()  # Renderizar o jogador
        # self.hud_renderer.desenhar_hud()  # Renderizar o HUD
        pygame.display.flip()
        pass