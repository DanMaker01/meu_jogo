import pygame

class Janela:
    def __init__(self, x, y, largura, altura, ativa=False, texto="", cor=(255, 255, 170)):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.ativa = ativa
        self.cor_coriginal = cor
        self.cor = cor
        self.cor_intensidade = 0  # Começa com a janela invisível
        self.fade_contador = 0
        self.texto = texto

    def fade_in(self, duracao=50):
        """Inicia o fade-in com uma duração específica."""
        self.fade_contador = duracao  # Quantos frames o fade vai durar
        self.cor_intensidade = 0  # Começa em 0 para o fade

    def ativar(self,duracao_fade=50):
        # self.ativa = True
        self.fade_in(duracao_fade)

    def desativar(self):
        self.ativa = False

    def draw(self, jogo):
        """Desenha a janela com a cor atual."""
        cor = (
            min(255, int(self.cor_intensidade * self.cor[0])),
            min(255, int(self.cor_intensidade * self.cor[1])),
            min(255, int(self.cor_intensidade * self.cor[2]))
        )

        if self.ativa:
            pygame.draw.rect(jogo.screen, cor, (self.x, self.y, self.largura, self.altura))

        if self.texto != "":
            label = jogo.font.render(self.texto, 1, (0, 0, 0))
            margemx = self.largura / 2 - label.get_width() / 2
            margemy = self.altura / 2 - label.get_height() / 2
            jogo.screen.blit(label, (self.x + margemx, self.y + margemy))

    def update(self):
        """Atualiza a janela, aplicando o efeito de fade-in."""
        if self.fade_contador > 0:
            self.fade_contador -= 1
            # Aumenta a intensidade da cor gradualmente
            if self.fade_contador > 0:
                self.ativa = True
                self.cor_intensidade = min(1, self.cor_intensidade + (1 / self.fade_contador))

    def set_cor(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

    def set_cor_original(self):
        self.cor = self.cor_coriginal

    def set_texto(self, texto):
        self.texto = texto

    def get_texto(self):
        return self.texto
