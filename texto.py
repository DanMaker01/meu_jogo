from janelas import Janela
import pygame

class Texto:
    def __init__(self, x, y, lar, alt, texto, nome, jogo, posicao_nome="supesq"):
        self.x = x
        self.y = y
        self.largura = lar
        self.altura = alt
        self.cor = (200, 200, 200)
        self.jogo = jogo
        # Janela de texto
        self.janela = Janela(self.x, self.y, self.largura, self.altura, texto="", cor=self.cor)

        # Fonte e cálculo da largura do nome
        self.fonte_nome = self.jogo.font  # fonte do nome
        self.largura_nome = self.calcular_largura_nome(nome)
        self.dimensoes_nome = (self.largura_nome, 24)  # Altura fixa para a janela do nome

        # Posição relativa da janela do nome
        self.pos_relativa_nome = self.calcular_posicao_nome(posicao_nome)

        # Janela de nome
        self.janela_nome = Janela(self.x + self.pos_relativa_nome[0], 
                                  self.y + self.pos_relativa_nome[1],
                                  self.dimensoes_nome[0], 
                                  self.dimensoes_nome[1], 
                                  texto="", cor=self.cor)

        self.texto = texto
        self.nome = nome

        # Animação
        self.alpha = 0  # Transparência inicial para o fade-in
        self.max_alpha = 255  # Transparência máxima
        self.fading_in = False  # Controle para o efeito de fade-in
        self.fade_speed = 0  # Velocidade do fade-in

        # Margens
        self.margem_x = 5
        self.margem_y = 5
        self.margem_x_nome = 5
        self.margem_y_nome = 2

    def calcular_largura_nome(self, nome):
        """
        Calcula a largura do nome usando a fonte definida.
        """
        largura_nome, _ = self.fonte_nome.size(nome)
        return largura_nome + 10  # Adiciona um pequeno espaço de margem para a largura

    def calcular_posicao_nome(self, posicao_nome):
        """
        Calcula a posição da janela do nome com base na escolha do usuário.
        """
        margem = 5
        posicoes = {
            "supdir": (self.largura - self.dimensoes_nome[0], -self.dimensoes_nome[1] - margem),
            "supesq": (0, -self.dimensoes_nome[1] - margem),
            "infdir": (self.largura - self.dimensoes_nome[0], self.altura + margem),
            "infesq": (0, self.altura + margem),
        }
        return posicoes.get(posicao_nome, posicoes["supdir"])  # Padrão: "supdir"

    def draw(self, jogo):
        # Atualiza o estado da janela e o controle de fade-in
        self.update()

        # Desenha as janelas
        self.janela.draw(jogo)
        self.janela_nome.draw(jogo)

        # Desenha o texto e o nome na tela com a mesma transparência (alpha)
        jogo.renderer.desenhar_texto(self.texto, self.x + self.margem_x, self.y + self.margem_y, 
                                     self.largura - self.margem_x, self.altura - self.margem_y, self.alpha)
        jogo.renderer.desenhar_texto(self.nome, 
                                     self.x + self.pos_relativa_nome[0] + self.margem_x_nome, 
                                     self.y + self.pos_relativa_nome[1] + self.margem_y_nome, 
                                     self.dimensoes_nome[0], self.dimensoes_nome[1], self.alpha)

    def update(self):
        # Atualiza as janelas e gerencia o fade-in do texto
        if self.janela:
            self.janela.update()
        if self.janela_nome:
            self.janela_nome.update()

        # Controle de fade-in do texto
        if self.fading_in and self.alpha < self.max_alpha:
            self.alpha = min(self.alpha + self.fade_speed, self.max_alpha)  # Limita o valor da alpha
            if self.alpha >= self.max_alpha:
                self.fading_in = False  # Finaliza o efeito de fade-in

    def ativar(self, duracao_fade=50, fps=1):
        """
        Ativa a janela e inicia o fade-in do texto e da janela. O fade-in vai durar duracao_fade segundos.
        
        :param duracao_fade: Tempo em segundos que o fade-in deve durar.
        :param fps: Quadros por segundo, usado para calcular a velocidade do fade.
        """
        # Ativa as janelas
        self.janela.ativar(duracao_fade, max_alpha=128)
        self.janela_nome.ativar(duracao_fade, max_alpha=128)

        # Calcula a velocidade do fade-in
        self.fade_speed = self.max_alpha / max(duracao_fade * fps, 1)  # Evita divisões por 0
        
        self.fading_in = True  # Inicia o fade-in do texto
        self.alpha = 0  # Começa com texto totalmente invisível

    def desativar(self):
        # Desativa as janelas
        self.janela.desativar()
        self.janela_nome.desativar()
