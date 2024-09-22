from janelas import Janela


class Pressao:
    def __init__(self, x,y,lar, alt):
        # print("iniciou classe Pressão")
        self.margem_x = 3
        self.margem_y = 3
        self.largura_max = lar-2*self.margem_x
        # x = 0
        # y = 0
        # lar = 100
        # alt = 30
        _cor_barra = (255, 220, 30) #amarelado

        self.janela = Janela(x, y, 
                             lar, alt, 
                             texto="", alpha=255)
        
        self.barra = Janela(x+self.margem_x, y+self.margem_y, 
                            lar-2*self.margem_x, alt - 2*self.margem_y, 
                            texto="", cor=_cor_barra, alpha=255)

        self.tempo = -1
        self.tempo_total = 0
        
        self.ativo = False
        self.tempo_ativo = False
        pass
    #--------------------------------------------------------------------------
    def avancar_tempo(self):    
        self.tempo -= 1
        tempo_percentual = self.tempo / self.tempo_total
        largura_percentual = tempo_percentual * self.largura_max
        self.barra.set_largura(largura_percentual)
        pass

    def resetar_tempo(self):
        self.tempo = self.tempo_total
        pass
    def zerar_tempo(self):
        self.tempo = 0
        pass
    def checar_se_tempo_acabou(self):
        if self.tempo == 0: return True
        else: return False
    #--------------------------------------------------------------------------
    def draw(self, jogo):
        if self.ativo:
            # print("desenha janelas da pressão")
            self.janela.draw(jogo)
            self.barra.draw(jogo)
        pass

   
    def update(self):
        
        if self.ativo:
            # self.barra.set
            self.janela.update()
            self.barra.update()

            if self.tempo_ativo:

                self.avancar_tempo()
                # print("tempo:", self.tempo)

                if self.checar_se_tempo_acabou():
                    self.desativar_tempo()
                    # self.zerar_tempo()
                    self.desativar()
                    
                    print("tempo acabou!!!!!!!!!!!")

        

        else:
            pass
            
            
    def ativar_tempo(self, tempo=200):
        # print("ativando tempo")
        self.tempo_total = tempo
        self.resetar_tempo()

        self.tempo_ativo = True
        print("pressão: tempo ativado:", self.tempo_total)

        pass
    def desativar_tempo(self):
        self.tempo_ativo = False
        self.zerar_tempo()
        pass
    def ativar(self):
        # print("ativar pressao")
        self.ativo = True
        # self.ativar_tempo(tempo)
        self.janela.ativar(duracao_fade=1)
        self.barra.ativar(duracao_fade=1)
        pass

    def desativar(self):
        # Desativa o Pressão
        # E o Janela e Barra
        self.ativo = False
        self.janela.desativar()
        self.barra.desativar()
        pass
 