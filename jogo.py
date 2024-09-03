import pygame
from controle import Controle
from recursos import Recursos
from renderer import Renderer
from opcoes import Opcoes
from texto import Texto
from janelas import Janela
from cena import GerenciadorCena
from roteiro import Roteiro

class Jogo:
    def __init__(self, width=800, height=600):
        print("iniciou classe Jogo")
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
        self.renderer = Renderer(self)
        # self.roteiro = Roteiro() #colocando dentro do Gerenciador Cena
        # Cena
        self.gerenciador_cena = GerenciadorCena(self)
        self.gerenciador_cena.carregar_cena(0)
        self.gerenciador_cena.ativar_cena_atual()
        
        # player    
    
        #animação #implementar depois
        #
        
        # Coloca o Jogo no Estado: Rodando!
        self.running = True
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
        self.controle.add_teclas_apertadas(pygame.key.name(key))
        # print(self.controle.get_teclas_apertadas())

    def draw(self):
        #implementar: adquirir todos objetos à serem desenhados e desenhar!
        #pode ser adicionando uma lista de imagens_a_desenhar dentro do renderer
        #ou algo do tipo.
        # (...)
        self.screen.fill(self.renderer.cor_neutra)  # Preenche a tela com a cor cinza
        self.renderer.desenhar_bg()
        # ---
        self.gerenciador_cena.draw(self)
        # self.janela_principal.draw(self)
        # self.texto.draw(self)
        # self.opcoes.draw(self)
        #----
        self.renderer.desenhar_hud()
        
        pygame.display.flip()
        pass

    def update(self):
        self.controle.update() 
        #...
        pass

    def run(self):
        """Loop principal do jogo."""
        while self.running:
            #loop principal
            # ---------------------------------------------
            # primeiro:
            # Verifica todos eventos que o jogo recebeu
            self.handle_events()
            self.clock.tick(60) # Controla a taxa de frames
            
            self.draw() # desenhar tudo primeiro
            # ---------------------------------------------
            # depois:
            self.update() #depois do draw
            
            # desenhar tudo
        
        # Encerra o Pygame ao sair do loop
        pygame.quit()