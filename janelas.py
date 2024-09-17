import pygame

class Janela:
    def __init__(self, x, y, largura, altura, ativa=False, texto="", cor=(200, 200, 200)):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        
        self.cor = cor
        self.cor_coriginal = cor
        self.ativa = ativa
        self.texto = texto
        self.alpha = 0  # Transparência inicial (0 = totalmente transparente)
        self.max_alpha = 255  # Transparência máxima (totalmente opaco)
        self.fading_in = False  # Controle de fade-in
        self.fade_speed = 0  # Velocidade do fade-in

    def set_alpha(self, alpha):
        self.alpha = alpha

    def ativar(self, duracao_fade=50, fps=1):
        """
        Ativa a janela e inicia o fade-in com base no valor de duracao_fade.
        
        :param duracao_fade: Duração do fade-in em segundos.
        :param fps: Quadros por segundo do jogo (para calcular a velocidade de fade).
        """
        print("ativou janela: ", self.get_texto(), "\t duracao_fade:",duracao_fade )
        self.ativa = True
        self.fading_in = True  # Começar o fade-in
        self.alpha = 0  # Iniciar com a janela totalmente transparente

        # Calcula a velocidade do fade com base na duração desejada e na taxa de quadros (fps)
        if duracao_fade == 0:
            print("janela tem que abrir em 0 seg")
            self.alpha = self.max_alpha
            self.fading_in = False  # Finaliza o fade-in
            self.ativa = True
        else:
            if duracao_fade < 1:
                duracao_fade = 1
            self.fade_speed = self.max_alpha / (duracao_fade * fps)

    def desativar(self):
        self.ativa = False

    def draw(self, jogo):
        if not self.ativa:
            return

        # Atualiza a cor com o valor de alfa (transparência)
        cor_transparente = (*self.cor[:3], self.alpha)  # Mantém os valores RGB e adiciona alfa
        
        # Cria uma superfície com canal alfa
        surface = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
        surface.fill(cor_transparente)  # Preenche a superfície com a cor e transparência
        jogo.screen.blit(surface, (self.x, self.y))  # Desenha a superfície com transparência

        if self.texto != "":
            # Desenha o texto no meio da janela
            label = jogo.font.render(self.texto, 1, (0, 0, 0))
            margemx = self.largura / 2 - label.get_width() / 2
            margemy = self.altura / 2 - label.get_height() / 2
            jogo.screen.blit(label, (self.x + margemx, self.y + margemy))

    def set_cor(self, cor):
        self.cor = cor

    def set_cor_original(self):
        self.cor = self.cor_coriginal

    def set_texto(self, texto):
        self.texto = texto

    def get_texto(self):
        return self.texto
    
    def update(self):
        # Incrementa o alfa durante o fade-in
        if self.fading_in and self.alpha < self.max_alpha:
            self.alpha += self.fade_speed
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha
                self.fading_in = False  # Finaliza o fade-in
        pass
