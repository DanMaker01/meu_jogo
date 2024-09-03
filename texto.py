import janelas
class Texto:
    def __init__(self, jogo):
        print("iniciou classe Texto")
        # self.jogo = jogo
        self.x = 90
        self.y= 410
        self.largura = 360
        self.altura = 120
        self.cor = (0, 0, 0)
        self.janela = janelas.Janela(self.x, self.y, self.largura, self.altura, texto="", cor=self.cor)
        self.texto = ""
        # self.janela = 

    def draw(self,jogo):
        self.janela.draw(jogo)
        pass

    def ativar(self):
        self.janela.ativar()
        pass
