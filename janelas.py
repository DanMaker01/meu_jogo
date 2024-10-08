import pygame

class Janela:
    def __init__(self, x, y, largura, altura, ativa=False, texto="", cor=(100, 100, 100), alpha=0):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        
        self.cor = cor
        self.cor_coriginal = cor
        self.ativa = ativa
        self.texto = texto
        self.alpha = alpha  # Transparência inicial (0 = totalmente transparente)
        self.max_alpha = 255  # Transparência máxima (totalmente opaco)
        self.fading_in = False  # Controle de fade-in
        self.fade_speed = 0  # Velocidade do fade-in

    def set_alpha(self, alpha):
        self.alpha = alpha

    def ativar_fade_in(self, duracao_fade=50, fps=1, max_alpha=255):
        self.fading_in = True       # Começar o fade-in
        self.alpha = 0              # Iniciar com a janela totalmente transparente
        self.max_alpha = max_alpha  # Definir a transparência máxima possível
        # Calcula a velocidade do fade com base na duração desejada e na taxa de quadros (fps)
        if duracao_fade == 0:
            self.alpha = self.max_alpha
            pass
        else:
            if duracao_fade < 1:
                duracao_fade = 1
            self.fade_speed = self.max_alpha / (duracao_fade * fps)

    def ativar(self, duracao_fade=50, fps=1, max_alpha=255):
        """
        Ativa a janela e
        Inicia o fade-in com base no valor de duracao_fade.
        
        :param duracao_fade: Duração do fade-in em segundos.
        :param fps: Quadros por segundo do jogo (para calcular a velocidade de fade).
        """
        # print("ativou janela: ", self.get_texto(), "\t duracao_fade:",duracao_fade )
        self.ativa = True
        self.ativar_fade_in(duracao_fade, fps, max_alpha)
        pass

    def desativar(self):
        self.ativa = False

    def draw(self, jogo):
        if not self.ativa: # se não tiver ativa, não desenha nada
            return

        # Atualiza a cor com o valor de alfa (transparência)
        cor_transparente = (*self.cor[:3], self.alpha)  # Mantém os valores RGB e adiciona alfa
        
        # Cria uma superfície com canal alfa
        surface = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
        surface.fill(cor_transparente)  # Preenche a superfície com a cor e transparência
        jogo.screen.blit(surface, (self.x, self.y))  # Desenha a superfície com transparência

        if self.texto != "":
            # aqui deve ser feito igual na classe Texto, pois o self.texto pode ficar maior que a janela #implementar
            # Desenha o texto no meio da janela
            label = jogo.font.render(self.texto, 1, (0, 0, 0))
            #centraliza na janela e desenha o texto.
            margemx = self.largura / 2 - label.get_width() / 2
            margemy = self.altura / 2 - label.get_height() / 2
            jogo.screen.blit(label, (self.x + margemx, self.y + margemy))

    def update(self):
        if not self.ativa: #
            return
        
        # Incrementa o alfa durante o fade-in
        if self.fading_in and self.alpha < self.max_alpha:
            self.alpha += self.fade_speed
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha
                self.fading_in = False  # Finaliza o fade-in
        pass

    def set_cor(self, cor):
        self.cor = cor

    def set_cor_original(self):
        self.cor = self.cor_coriginal

    def set_texto(self, texto):
        self.texto = texto

    def get_texto(self):
        return self.texto
    
    def set_largura(self, largura):
        if largura < 0:
            largura = 0

        self.largura = largura