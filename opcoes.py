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

        margem_x = 2
        margem_y = 2
        for i in range(len(self.opcoes)):
            _x = pos_x+margem_x
            _y = pos_y + self.distancia_entre_opcoes*i + 1/2 *margem_y
            _largura = largura- 2*margem_x
            _altura = alt/len(self.opcoes) - margem_y
            _texto = self.opcoes[i][0]
            _cor = (255,255,255)
            self.opcoes_janelas.append(Janela(_x,_y,_largura,_altura,texto=_texto, cor=_cor))

        self.opcao_selecionada = 0
        # self.janelas_opcoes = []
        pass
    

    def ativar(self, duracao_fade=50):
        self.janela.ativar(duracao_fade)
        for i in range(len(self.opcoes_janelas)):
            self.opcoes_janelas[i].ativar(duracao_fade+5*i)
        pass
    def desativar(self):
        self.janela.desativar()
        pass
    def adicionar_opcao(self, texto, direcao):
        self.opcoes.append([texto, direcao])
                
        pass
    def limpar_opcoes(self):
        self.opcoes = []
        pass
    def get_opcoes(self):
        return self.opcoes

    def get_opcoes_qtd(self):
        return len(self.opcoes)

    def set_opcao_escolhida(self, indice):
        self.opcao_escolhida = indice
        pass
    def get_opcao_selecionada(self):
        return self.opcao_selecionada

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
        if self.janela.ativa == True:
            self.janela.draw(jogo) #cor de fundo das opções 
            
            if self.opcoes: # se tiver alguma opcão
                for janela in self.opcoes_janelas: # desenha cada janela de opção
                    #se é o indice da janela que está selecionada, desenha a opção em verde
                    if self.opcao_selecionada == self.opcoes_janelas.index(janela):
                        janela.set_cor((0,170,0))
                    else:
                        janela.set_cor_original()

                    #se o texto da janela estiver vazio, coloca '>>'
                    if janela.get_texto() == "":
                        janela.set_texto(">>")
                    janela.draw(jogo)
            else:
                print("Nenhuma opção definida")
        



        else: #não está visível as opções
    
            pass

    def update(self):
        if self.janela:
            self.janela.update()
        
        for janela_opcao in self.opcoes_janelas:
            janela_opcao.update()
            
        pass
    