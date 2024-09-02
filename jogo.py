import pygame
from controle import Controle
from recursos import Recursos

class Jogo:
    def __init__(self, width=800, height=600):
        pygame.init()
        pygame.display.set_caption("Meu Jogo")
        
        # Configurações da janela visível na tela
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        # Fonte para texto
        self.font = pygame.font.SysFont(None, 20)

        # Configuração do relógio para controlar a taxa de frames
        self.clock = pygame.time.Clock()

        # Gerenciadores
        self.controle = Controle()
        self.recursos = Recursos()
        #roteiro
        #cena
        #player
        #animação #implementar depois
        #
        
        # Coloca o Jogo no Estado: Rodando!
        self.running = True
        print("iniciou classe Jogo")
        pass 

    def handle_events(self):
        """Gerencia os eventos do jogo, como fechar a janela ou pressionar teclas."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):
        """Função para lidar com eventos de pressionamento de teclas."""
        # Aqui você pode adicionar manipulação de eventos de teclado
        print(f"Tecla pressionada: {pygame.key.name(key)}")
        self.controle.add_teclas_apertadas(pygame.key.name(key))
        # print(self.controle.get_teclas_apertadas())

    def run(self):
        """Loop principal do jogo."""
        while self.running:
            self.handle_events()
            # Limpa a tela a cada frame
            self.screen.fill((0, 0, 0))  # Preenche a tela com a cor preta
            # Atualiza a tela
            pygame.display.flip()
            # Controla a taxa de frames
            self.clock.tick(60)
        
        # Encerra o Pygame ao sair do loop
        pygame.quit()