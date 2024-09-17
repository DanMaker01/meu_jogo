import janelas

class Palco:
    def __init__(self, x, y, lar, alt, imagem_id):
        # print("iniciou classe Palco")
        self.x = x
        self.y = y
        self.largura = lar
        self.altura = alt
        # self.cor = (2, 2, 2)
        self.cor = (245, 245, 245)

        self.margem_x = 2
        self.margem_y = 2

        self.janela = janelas.Janela(self.x, self.y, self.largura+2*self.margem_x, self.altura+2*self.margem_y, texto="", cor=self.cor)
        self.imagem_id = imagem_id
        self.alpha = 0  # Transparência inicial para o fade-in
        self.max_alpha = 255  # Transparência máxima
        self.fading_in = False  # Controle para o efeito de fade-in
        pass

    def draw(self, jogo):
        # Desenha a janela
        self.janela.draw(jogo)
        
        if self.alpha == 0: #não parece mto certo  #implementar
            self.alpha = 255
        
        # Desenha a imagem com o valor atual de transparência (alpha)
        if self.imagem_id:
            jogo.renderer.desenhar_imagem(self.imagem_id, self.x+self.margem_x, self.y+self.margem_y, self.alpha)

    def update(self):
        # Atualiza a janela (para o fade-in da janela)
        if self.janela:
            self.janela.update()

        # Controle de fade-in da imagem
        if self.fading_in and self.alpha < self.max_alpha:
            self.alpha += self.fade_speed  # Incrementa a transparência
            if self.alpha >= self.max_alpha:
                self.alpha = self.max_alpha  # Garante que não ultrapasse o valor máximo
                self.fading_in = False  # Finaliza o efeito de fade-in


    def ativar(self, duracao_fade=50, fps=1):
        """
        Ativa a janela e inicia o fade-in da imagem. O fade-in vai durar duracao_fade segundos.
        
        :param duracao_fade: Tempo em segundos que o fade-in deve durar.
        :param fps: Quadros por segundo, usado para calcular a velocidade do fade.
        """
        # Ativa a janela e o fade-in da imagem
        self.janela.ativar(duracao_fade)
        if duracao_fade > 0:

            if duracao_fade == 0:
                duracao_fade = 1
            # Calcula a velocidade do fade-in baseada na duração
            self.fade_speed = self.max_alpha / (duracao_fade * fps)
            
            self.fading_in = True  # Inicia o fade-in da imagem
            self.alpha = 0  # Inicia a imagem com transparência total (invisível)
        else:
            self.alpha = self.max_alpha
            self.fading_in = False 

    def desativar(self):
        # Desativa a janela
        self.janela.desativar()
