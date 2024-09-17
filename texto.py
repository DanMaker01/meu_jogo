import janelas

class Texto:
    def __init__(self, x, y, lar, alt, texto):
        # print("iniciou classe Texto")
        self.x = x
        self.y = y
        self.largura = lar
        self.altura = alt
        self.cor = ( 200, 200,200)
        self.janela = janelas.Janela(self.x, self.y, self.largura, self.altura, texto="", cor=self.cor)
        self.texto = texto
        self.alpha = 0  # Transparência inicial para o fade-in
        self.max_alpha = 255  # Transparência máxima
        self.fading_in = False  # Controle para o efeito de fade-in
        self.fade_speed = 0  # Velocidade do fade-in

    def draw(self, jogo):
        # Atualiza o estado da janela e o controle de fade-in
        self.update()

        # Desenha a janela com a transparência atual
        self.janela.draw(jogo)

        # Desenha o texto na tela com a mesma transparência (alpha)
        margem_x = 5
        margem_y = 5
        # print(self.texto)
        jogo.renderer.desenhar_texto(self.texto, self.x + margem_x, self.y + margem_y, 360 - margem_x, 120 - margem_y, self.alpha)

    def update(self):
        if self.janela:
            self.janela.update()
        
        # Controle de fade-in do texto
        if self.fading_in and self.alpha < self.max_alpha:
            self.alpha += self.fade_speed
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha
                self.fading_in = False  # Finaliza o efeito de fade-in

    def ativar(self, duracao_fade=50, fps=1):
        """
        Ativa a janela e inicia o fade-in do texto e da janela. O fade-in vai durar duracao_fade segundos.
        
        :param duracao_fade: Tempo em segundos que o fade-in deve durar.
        :param fps: Quadros por segundo, usado para calcular a velocidade do fade.
        """
        # Ativa a janela e o fade-in do texto
        self.janela.ativar(duracao_fade, max_alpha=128)
        
        if duracao_fade < 1:
            duracao_fade = 1
        # Calcula a velocidade do fade-in baseada na duração
        self.fade_speed = self.max_alpha / (duracao_fade * fps)
        
        self.fading_in = True  # Inicia o fade-in do texto
        self.alpha = 0  # Inicia o texto com transparência total (invisível)

    def desativar(self):
        # Desativa a janela
        self.janela.desativar()
