import pygame
from controle import Controle
from recursos import Recursos
from renderer import Renderer
# from opcoes import Opcoes
# from texto import Texto
# from janelas import Janela
from cena import GerenciadorCena
from roteiro import Roteiro
from historico import Historico
from modificadores import GerenciadorMods
from memoria import Memoria
# from pressao import Pressao

class Jogo:
    def __init__(self, width=800, height=600):
        # print("iniciou classe Jogo")
        pygame.init()
        pygame.display.set_caption("Meu Jogo - Daemon - Anomia")
        
        # Configurações da janela visível na tela
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        # Fonte para texto
        fontes_disponiveis = pygame.font.get_fonts()
        selecionar_fonte = 0 # a fonte 0 normalmente é Arial
        self.font = pygame.font.SysFont(fontes_disponiveis[selecionar_fonte], 16)
        
        # Configuração do relógio para controlar a taxa de frames
        self.clock = pygame.time.Clock()

        # Gerenciadores
        self.controle = Controle()
        self.recursos = Recursos()
        self.renderer = Renderer(self)
        self.roteiro = Roteiro()
        self.historico = Historico()
        self.modificadores = GerenciadorMods()
        self.memoria = Memoria(self, 'save1.dat')
        # self.pressao = Pressao()
        
        #teste roteiro
        # print("roteiro org[1]",self.roteiro.get_roteiro_organizado()[1]

        # # player é onde tem os modificadores?
        self.modificadores.alterar_mod("vida",1)
        self.modificadores.alterar_mod("moeda de prata",10)
        self.modificadores.alterar_mod("batata (kg)",1.473)
        self.modificadores.alterar_mod("dor",0)
        #animação-renderer #implementar depois
        
        # Cena
        self.gerenciador_cena = GerenciadorCena(self)
        # self.gerenciador_cena.carregar_cena(1)
        self.gerenciador_cena.carregar_cena(2)
        self.gerenciador_cena.ativar_cena_atual()
        
        
        self.running = True #iniciar loop principal
        pass 


    def handle_events(self):
        """Gerencia os eventos do jogo, como fechar a janela ou pressionar teclas."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                print("saindo do jogo...")
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
        self.gerenciador_cena.draw(self)
        self.renderer.desenhar_hud()
        
        pygame.display.flip()
        pass

    def update(self): #implementar
        self.controle.update()
        # self.clock.tick(30)
         
        
        if self.gerenciador_cena.is_possivel_interagir():
            # self.pressao.update()
            self.verifica_acao_jogador()
        
        #...
        self.gerenciador_cena.update()
        self.controle.limpar_teclas_apertadas()
        pass

    def verifica_acao_jogador(self):
        #
        acao_feita = self.controle.verifica_teclas()
        if acao_feita == 'confirma':
            self.gerenciador_cena.confirmar_opcao()
            self.gerenciador_cena.ativar_cena_atual()
            
        elif acao_feita == 'acima':
            self.gerenciador_cena.cena_atual.get_opcoes().selecionar_atras()
        elif acao_feita == 'abaixo':
            self.gerenciador_cena.cena_atual.get_opcoes().selecionar_afrente()
        elif acao_feita == 'salvar':
            self.memoria.salvar()
        elif acao_feita == 'carregar':#implementar a Pressão
            self.memoria.carregar()
            self.gerenciador_cena.carregar_cena(self.historico.get_ultima_cena())
            self.gerenciador_cena.ativar_cena_atual()
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
