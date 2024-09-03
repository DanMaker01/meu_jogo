#classe Opções
from janelas import Janela

class Opcoes:
    def __init__(self,x,y,lar,alt,opcoes):
        print("iniciou classe Opções")
        
        pos_x = x
        pos_y = y
        largura = lar
        altura = alt
        _cor = (200,200,200)
        self.janela = Janela(pos_x, pos_y, largura, altura,cor=_cor)
        
        self.visivel = True

        self.ativar_interacao = False

        self.opcoes = opcoes
        self.opcoes_janelas = []
        self.distancia_entre_opcoes = alt/len(self.opcoes)

        for i in range(len(self.opcoes)):
            _x = pos_x
            _y = pos_y + self.distancia_entre_opcoes*i
            _largura = largura
            _altura = alt/len(self.opcoes)
            _texto = self.opcoes[i][0]
            _cor = (255,255,255)
            print(_x,_y,_largura,_altura, _texto)
            self.opcoes_janelas.append(Janela(_x,_y,_largura,_altura, texto=_texto, cor=_cor))

        self.opcao_selecionada = 0
        self.opcao_escolhida = 0
        # self.janelas_opcoes = []
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
                for janela in self.opcoes_janelas:
                    janela.draw(jogo)
                pass
            pass
        else:
            pass

    def update(self):

        pass
    