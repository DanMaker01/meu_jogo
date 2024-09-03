#classe Opções
import janelas

class Opcoes:
    def __init__(self):
        print("iniciou classe Opções")
        
        pos_x = 540
        pos_y = 200
        largura = 230
        altura = 192
        self.janela = janelas.Janela(pos_x, pos_y, largura, altura,cor=(0,0,0))
        
        self.visivel = True

        self.ativar_interacao = False

        self.distancia_entre_opcoes = 5
        self.opcao_selecionada = 0
        self.opcao_escolhida = 0
        self.opcoes = [] # elementos no formato: ["texto0",direcao0,janela0] , ["texto1",direcao1,janela1], ...         
        self.janelas_opcoes = []
        pass
    
    def ativar(self):
        self.janela.ativar()

    def adicionar_opcao(self, texto, direcao):
        self.opcoes.append([texto, direcao])
                
        pass
    def limpar_opcoes(self):
        self.opcoes = []
        pass
    def get_opcoes(self):
        return self.opcoes


    def set_opcao_escolhida(self, indice):
        self.opcao_escolhida = indice
        pass
    def get_opcao_escolhida(self):
        return self.opcao_escolhida

    def selecionar_afrente(self):
        self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes)
        pass
    def selecionar_atras(self):
        self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes)
        pass
    def selecionar_opcao(self, indice):
        self.opcao_selecionada = indice
        pass
    def draw(self, jogo):
        # mostrar a opção selecionada bem chamativa
        # #implementar
        # (...)
        self.janela.draw(jogo) #cor de fundo das opções 

        if self.visivel == True:
            if self.opcoes:
                print("print opcoes",self.opcoes)
                
            pass
        else:
            pass

    def update(self):

        pass
    